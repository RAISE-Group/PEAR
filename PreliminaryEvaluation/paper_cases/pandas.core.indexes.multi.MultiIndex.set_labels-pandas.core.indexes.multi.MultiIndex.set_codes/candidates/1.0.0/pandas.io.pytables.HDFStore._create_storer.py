def _create_storer(self, group, format=None, value: Optional[FrameOrSeries]=None, encoding: str='UTF-8', errors: str='strict') -> Union['GenericFixed', 'Table']:
    """ return a suitable class to operate """
    cls: Union[Type['GenericFixed'], Type['Table']]
    if value is not None and (not isinstance(value, (Series, DataFrame))):
        raise TypeError('value must be None, Series, or DataFrame')

    def error(t):
        return TypeError(f'cannot properly create the storer for: [{t}] [group->{group},value->{type(value)},format->{format}')
    pt = _ensure_decoded(getattr(group._v_attrs, 'pandas_type', None))
    tt = _ensure_decoded(getattr(group._v_attrs, 'table_type', None))
    if pt is None:
        if value is None:
            _tables()
            assert _table_mod is not None
            if getattr(group, 'table', None) or isinstance(group, _table_mod.table.Table):
                pt = 'frame_table'
                tt = 'generic_table'
            else:
                raise TypeError('cannot create a storer if the object is not existing nor a value are passed')
        else:
            _TYPE_MAP = {Series: 'series', DataFrame: 'frame'}
            pt = _TYPE_MAP[type(value)]
            if format == 'table':
                pt += '_table'
    if 'table' not in pt:
        _STORER_MAP = {'series': SeriesFixed, 'frame': FrameFixed}
        try:
            cls = _STORER_MAP[pt]
        except KeyError:
            raise error('_STORER_MAP')
        return cls(self, group, encoding=encoding, errors=errors)
    if tt is None:
        if value is not None:
            if pt == 'series_table':
                index = getattr(value, 'index', None)
                if index is not None:
                    if index.nlevels == 1:
                        tt = 'appendable_series'
                    elif index.nlevels > 1:
                        tt = 'appendable_multiseries'
            elif pt == 'frame_table':
                index = getattr(value, 'index', None)
                if index is not None:
                    if index.nlevels == 1:
                        tt = 'appendable_frame'
                    elif index.nlevels > 1:
                        tt = 'appendable_multiframe'
    _TABLE_MAP = {'generic_table': GenericTable, 'appendable_series': AppendableSeriesTable, 'appendable_multiseries': AppendableMultiSeriesTable, 'appendable_frame': AppendableFrameTable, 'appendable_multiframe': AppendableMultiFrameTable, 'worm': WORMTable}
    try:
        cls = _TABLE_MAP[tt]
    except KeyError:
        raise error('_TABLE_MAP')
    return cls(self, group, encoding=encoding, errors=errors)