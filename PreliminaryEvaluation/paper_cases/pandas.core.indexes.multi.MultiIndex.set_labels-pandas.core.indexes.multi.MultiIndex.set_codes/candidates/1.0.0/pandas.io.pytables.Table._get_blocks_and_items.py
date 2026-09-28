@staticmethod
def _get_blocks_and_items(block_obj, table_exists, new_non_index_axes, values_axes, data_columns):

    def get_blk_items(mgr, blocks):
        return [mgr.items.take(blk.mgr_locs) for blk in blocks]
    blocks = block_obj._data.blocks
    blk_items = get_blk_items(block_obj._data, blocks)
    if len(data_columns):
        axis, axis_labels = new_non_index_axes[0]
        new_labels = Index(axis_labels).difference(Index(data_columns))
        mgr = block_obj.reindex(new_labels, axis=axis)._data
        blocks = list(mgr.blocks)
        blk_items = get_blk_items(mgr, blocks)
        for c in data_columns:
            mgr = block_obj.reindex([c], axis=axis)._data
            blocks.extend(mgr.blocks)
            blk_items.extend(get_blk_items(mgr, mgr.blocks))
    if table_exists:
        by_items = {tuple(b_items.tolist()): (b, b_items) for b, b_items in zip(blocks, blk_items)}
        new_blocks = []
        new_blk_items = []
        for ea in values_axes:
            items = tuple(ea.values)
            try:
                b, b_items = by_items.pop(items)
                new_blocks.append(b)
                new_blk_items.append(b_items)
            except (IndexError, KeyError):
                jitems = ','.join((pprint_thing(item) for item in items))
                raise ValueError(f'cannot match existing table structure for [{jitems}] on appending data')
        blocks = new_blocks
        blk_items = new_blk_items
    return (blocks, blk_items)