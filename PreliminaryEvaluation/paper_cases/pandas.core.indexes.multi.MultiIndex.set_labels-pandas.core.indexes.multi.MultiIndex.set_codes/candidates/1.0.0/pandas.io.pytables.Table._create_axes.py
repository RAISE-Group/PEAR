def _create_axes(self, axes, obj: DataFrame, validate: bool=True, nan_rep=None, data_columns=None, min_itemsize=None):
    """
        Create and return the axes.

        Parameters
        ----------
        axes: list or None
            The names or numbers of the axes to create.
        obj : DataFrame
            The object to create axes on.
        validate: bool, default True
            Whether to validate the obj against an existing object already written.
        nan_rep :
            A value to use for string column nan_rep.
        data_columns : List[str], True, or None, default None
            Specify the columns that we want to create to allow indexing on.

            * True : Use all available columns.
            * None : Use no columns.
            * List[str] : Use the specified columns.

        min_itemsize: Dict[str, int] or None, default None
            The min itemsize for a column in bytes.
        """
    if not isinstance(obj, DataFrame):
        group = self.group._v_name
        raise TypeError(f'cannot properly create the storer for: [group->{group},value->{type(obj)}]')
    if axes is None:
        axes = [0]
    axes = [obj._get_axis_number(a) for a in axes]
    if self.infer_axes():
        table_exists = True
        axes = [a.axis for a in self.index_axes]
        data_columns = list(self.data_columns)
        nan_rep = self.nan_rep
    else:
        table_exists = False
    new_info = self.info
    assert self.ndim == 2
    if len(axes) != self.ndim - 1:
        raise ValueError('currently only support ndim-1 indexers in an AppendableTable')
    new_non_index_axes: List = []
    if nan_rep is None:
        nan_rep = 'nan'
    idx = [x for x in [0, 1] if x not in axes][0]
    a = obj.axes[idx]
    append_axis = list(a)
    if table_exists:
        indexer = len(new_non_index_axes)
        exist_axis = self.non_index_axes[indexer][1]
        if not array_equivalent(np.array(append_axis), np.array(exist_axis)):
            if array_equivalent(np.array(sorted(append_axis)), np.array(sorted(exist_axis))):
                append_axis = exist_axis
    info = new_info.setdefault(idx, {})
    info['names'] = list(a.names)
    info['type'] = type(a).__name__
    new_non_index_axes.append((idx, append_axis))
    idx = axes[0]
    a = obj.axes[idx]
    axis_name = obj._AXIS_NAMES[idx]
    new_index = _convert_index(axis_name, a, self.encoding, self.errors)
    new_index.axis = idx
    new_index.set_pos(0)
    new_index.update_info(new_info)
    new_index.maybe_set_size(min_itemsize)
    new_index_axes = [new_index]
    j = len(new_index_axes)
    assert j == 1
    assert len(new_non_index_axes) == 1
    for a in new_non_index_axes:
        obj = _reindex_axis(obj, a[0], a[1])

    def get_blk_items(mgr, blocks):
        return [mgr.items.take(blk.mgr_locs) for blk in blocks]
    transposed = new_index.axis == 1
    data_columns = self.validate_data_columns(data_columns, min_itemsize, new_non_index_axes)
    block_obj = self.get_object(obj, transposed)._consolidate()
    blocks, blk_items = self._get_blocks_and_items(block_obj, table_exists, new_non_index_axes, self.values_axes, data_columns)
    vaxes = []
    for i, (b, b_items) in enumerate(zip(blocks, blk_items)):
        klass = DataCol
        name = None
        if data_columns and len(b_items) == 1 and (b_items[0] in data_columns):
            klass = DataIndexableCol
            name = b_items[0]
            if not (name is None or isinstance(name, str)):
                raise ValueError('cannot have non-object label DataIndexableCol')
        existing_col: Optional[DataCol]
        if table_exists and validate:
            try:
                existing_col = self.values_axes[i]
            except (IndexError, KeyError):
                raise ValueError(f'Incompatible appended table [{blocks}]with existing table [{self.values_axes}]')
        else:
            existing_col = None
        new_name = name or f'values_block_{i}'
        data_converted = _maybe_convert_for_string_atom(new_name, b, existing_col=existing_col, min_itemsize=min_itemsize, nan_rep=nan_rep, encoding=self.encoding, errors=self.errors)
        adj_name = _maybe_adjust_name(new_name, self.version)
        typ = klass._get_atom(data_converted)
        kind = _dtype_to_kind(data_converted.dtype.name)
        tz = _get_tz(data_converted.tz) if hasattr(data_converted, 'tz') else None
        meta = metadata = ordered = None
        if is_categorical_dtype(data_converted):
            ordered = data_converted.ordered
            meta = 'category'
            metadata = np.array(data_converted.categories, copy=False).ravel()
        data, dtype_name = _get_data_and_dtype_name(data_converted)
        col = klass(name=adj_name, cname=new_name, values=list(b_items), typ=typ, pos=j, kind=kind, tz=tz, ordered=ordered, meta=meta, metadata=metadata, dtype=dtype_name, data=data)
        col.update_info(new_info)
        vaxes.append(col)
        j += 1
    dcs = [col.name for col in vaxes if col.is_data_indexable]
    new_table = type(self)(parent=self.parent, group=self.group, encoding=self.encoding, errors=self.errors, index_axes=new_index_axes, non_index_axes=new_non_index_axes, values_axes=vaxes, data_columns=dcs, info=new_info, nan_rep=nan_rep)
    if hasattr(self, 'levels'):
        new_table.levels = self.levels
    new_table.validate_min_itemsize(min_itemsize)
    if validate and table_exists:
        new_table.validate(self)
    return new_table