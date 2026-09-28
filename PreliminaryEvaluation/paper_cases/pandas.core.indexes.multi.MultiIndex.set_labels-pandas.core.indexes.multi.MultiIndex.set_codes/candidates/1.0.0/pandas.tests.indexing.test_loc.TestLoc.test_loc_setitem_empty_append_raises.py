def test_loc_setitem_empty_append_raises(self):
    data = [1, 2]
    df = DataFrame(columns=['x', 'y'])
    msg = "None of \\[Int64Index\\(\\[0, 1\\], dtype='int64'\\)\\] are in the \\[index\\]"
    with pytest.raises(KeyError, match=msg):
        df.loc[[0, 1], 'x'] = data
    msg = 'cannot copy sequence with size 2 to array axis with dimension 0'
    with pytest.raises(ValueError, match=msg):
        df.loc[0:2, 'x'] = data