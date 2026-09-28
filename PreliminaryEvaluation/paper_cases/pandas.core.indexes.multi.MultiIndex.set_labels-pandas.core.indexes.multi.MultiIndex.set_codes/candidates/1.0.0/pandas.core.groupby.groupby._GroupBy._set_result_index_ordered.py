def _set_result_index_ordered(self, result):
    if not self.grouper.is_monotonic:
        index = Index(np.concatenate(self._get_indices(self.grouper.result_index)))
        result.set_axis(index, axis=self.axis, inplace=True)
        result = result.sort_index(axis=self.axis)
    result.set_axis(self.obj._get_axis(self.axis), axis=self.axis, inplace=True)
    return result