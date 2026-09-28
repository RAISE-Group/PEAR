def quantile(self, qs, interpolation='linear', axis=0):
    naive = self.values.view('M8[ns]')
    naive = naive.reshape(self.shape)
    blk = self.make_block(naive)
    res_blk = blk.quantile(qs, interpolation=interpolation, axis=axis)
    aware = self._holder(res_blk.values.ravel(), dtype=self.dtype)
    return self.make_block_same_class(aware, ndim=res_blk.ndim)