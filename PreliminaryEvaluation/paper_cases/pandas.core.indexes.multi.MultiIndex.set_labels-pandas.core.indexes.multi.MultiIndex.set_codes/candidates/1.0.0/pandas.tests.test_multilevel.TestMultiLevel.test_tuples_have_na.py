def test_tuples_have_na(self):
    index = MultiIndex(levels=[[1, 0], [0, 1, 2, 3]], codes=[[1, 1, 1, 1, -1, 0, 0, 0], [0, 1, 2, 3, 0, 1, 2, 3]])
    assert isna(index[4][0])
    assert isna(index.values[4][0])