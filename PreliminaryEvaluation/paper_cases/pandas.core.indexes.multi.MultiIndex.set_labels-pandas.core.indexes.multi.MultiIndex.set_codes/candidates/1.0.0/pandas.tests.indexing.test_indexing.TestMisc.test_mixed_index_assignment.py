def test_mixed_index_assignment(self):
    s = Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 1, 2])
    s.at['a'] = 11
    assert s.iat[0] == 11
    s.at[1] = 22
    assert s.iat[3] == 22