def test_loc_preserve_names(self):
    result = self.ymd.loc[2000]
    result2 = self.ymd['A'].loc[2000]
    assert result.index.names == self.ymd.index.names[1:]
    assert result2.index.names == self.ymd.index.names[1:]
    result = self.ymd.loc[2000, 2]
    result2 = self.ymd['A'].loc[2000, 2]
    assert result.index.name == self.ymd.index.names[2]
    assert result2.index.name == self.ymd.index.names[2]