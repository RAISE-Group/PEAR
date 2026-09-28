def test_loc_to_fail(self):
    df = DataFrame(np.random.random((3, 3)), index=['a', 'b', 'c'], columns=['e', 'f', 'g'])
    msg = '\\"None of \\[Int64Index\\(\\[1, 2\\], dtype=\'int64\'\\)\\] are in the \\[index\\]\\"'
    with pytest.raises(KeyError, match=msg):
        df.loc[[1, 2], [1, 2]]
    s = Series(dtype=object)
    s.loc[1] = 1
    s.loc['a'] = 2
    with pytest.raises(KeyError, match='^-1$'):
        s.loc[-1]
    msg = '\\"None of \\[Int64Index\\(\\[-1, -2\\], dtype=\'int64\'\\)\\] are in the \\[index\\]\\"'
    with pytest.raises(KeyError, match=msg):
        s.loc[[-1, -2]]
    msg = '\\"None of \\[Index\\(\\[\'4\'\\], dtype=\'object\'\\)\\] are in the \\[index\\]\\"'
    with pytest.raises(KeyError, match=msg):
        s.loc[['4']]
    s.loc[-1] = 3
    with pytest.raises(KeyError, match='with any missing labels'):
        s.loc[[-1, -2]]
    s['a'] = 2
    msg = '\\"None of \\[Int64Index\\(\\[-2\\], dtype=\'int64\'\\)\\] are in the \\[index\\]\\"'
    with pytest.raises(KeyError, match=msg):
        s.loc[[-2]]
    del s['a']
    with pytest.raises(KeyError, match=msg):
        s.loc[[-2]] = 0
    df = DataFrame([['a'], ['b']], index=[1, 2], columns=['value'])
    msg = '\\"None of \\[Int64Index\\(\\[3\\], dtype=\'int64\'\\)\\] are in the \\[index\\]\\"'
    with pytest.raises(KeyError, match=msg):
        df.loc[[3], :]
    with pytest.raises(KeyError, match=msg):
        df.loc[[3]]