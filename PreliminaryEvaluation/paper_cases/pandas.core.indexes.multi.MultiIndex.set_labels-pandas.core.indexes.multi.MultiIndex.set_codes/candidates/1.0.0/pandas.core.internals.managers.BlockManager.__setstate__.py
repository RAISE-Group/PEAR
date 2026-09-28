def __setstate__(self, state):

    def unpickle_block(values, mgr_locs):
        return make_block(values, placement=mgr_locs)
    if isinstance(state, tuple) and len(state) >= 4 and ('0.14.1' in state[3]):
        state = state[3]['0.14.1']
        self.axes = [ensure_index(ax) for ax in state['axes']]
        self.blocks = tuple((unpickle_block(b['values'], b['mgr_locs']) for b in state['blocks']))
    else:
        ax_arrays, bvalues, bitems = state[:3]
        self.axes = [ensure_index(ax) for ax in ax_arrays]
        if len(bitems) == 1 and self.axes[0].equals(bitems[0]):
            all_mgr_locs = [slice(0, len(bitems[0]))]
        else:
            all_mgr_locs = [self.axes[0].get_indexer(blk_items) for blk_items in bitems]
        self.blocks = tuple((unpickle_block(values, mgr_locs) for values, mgr_locs in zip(bvalues, all_mgr_locs)))
    self._post_setstate()