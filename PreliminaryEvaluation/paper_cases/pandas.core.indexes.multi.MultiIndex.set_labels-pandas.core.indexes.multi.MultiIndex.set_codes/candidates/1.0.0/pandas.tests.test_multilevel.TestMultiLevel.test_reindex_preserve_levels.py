def test_reindex_preserve_levels(self):
    new_index = self.ymd.index[::10]
    chunk = self.ymd.reindex(new_index)
    assert chunk.index is new_index
    chunk = self.ymd.loc[new_index]
    assert chunk.index is new_index
    ymdT = self.ymd.T
    chunk = ymdT.reindex(columns=new_index)
    assert chunk.columns is new_index
    chunk = ymdT.loc[:, new_index]
    assert chunk.columns is new_index