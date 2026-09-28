def get_reindexed_values(self, empty_dtype, upcasted_na):
    if upcasted_na is None:
        fill_value = self.block.fill_value
        values = self.block.get_values()
    else:
        fill_value = upcasted_na
        if self.is_na:
            if getattr(self.block, 'is_object', False):
                values = self.block.values.ravel(order='K')
                if len(values) and values[0] is None:
                    fill_value = None
            if getattr(self.block, 'is_datetimetz', False) or is_datetime64tz_dtype(empty_dtype):
                if self.block is None:
                    array = empty_dtype.construct_array_type()
                    return array(np.full(self.shape[1], fill_value.value), dtype=empty_dtype)
            elif getattr(self.block, 'is_categorical', False):
                pass
            elif getattr(self.block, 'is_extension', False):
                pass
            else:
                missing_arr = np.empty(self.shape, dtype=empty_dtype)
                missing_arr.fill(fill_value)
                return missing_arr
        if not self.indexers:
            if not self.block._can_consolidate:
                return self.block.values
        if self.block.is_bool and (not self.block.is_categorical):
            values = self.block.astype(np.object_).values
        elif self.block.is_extension:
            values = self.block.values
        else:
            values = self.block.get_values()
    if not self.indexers:
        values = values.view()
    else:
        for ax, indexer in self.indexers.items():
            values = algos.take_nd(values, indexer, axis=ax, fill_value=fill_value)
    return values