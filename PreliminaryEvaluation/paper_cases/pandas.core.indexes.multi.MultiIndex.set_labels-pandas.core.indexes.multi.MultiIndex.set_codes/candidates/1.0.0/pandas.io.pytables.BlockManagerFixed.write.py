def write(self, obj, **kwargs):
    super().write(obj, **kwargs)
    data = obj._data
    if not data.is_consolidated():
        data = data.consolidate()
    self.attrs.ndim = data.ndim
    for i, ax in enumerate(data.axes):
        if i == 0:
            if not ax.is_unique:
                raise ValueError('Columns index has to be unique for fixed format')
        self.write_index(f'axis{i}', ax)
    self.attrs.nblocks = len(data.blocks)
    for i, blk in enumerate(data.blocks):
        blk_items = data.items.take(blk.mgr_locs)
        self.write_array(f'block{i}_values', blk.values, items=blk_items)
        self.write_index(f'block{i}_items', blk_items)