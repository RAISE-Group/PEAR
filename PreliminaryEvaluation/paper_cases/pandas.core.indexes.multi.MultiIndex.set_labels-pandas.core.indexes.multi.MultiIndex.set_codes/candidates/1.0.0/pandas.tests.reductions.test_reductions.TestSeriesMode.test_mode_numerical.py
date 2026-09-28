@pytest.mark.parametrize('dropna, data, expected', [(True, [1, 1, 1, 2], [1]), (True, [1, 1, 1, 2, 3, 3, 3], [1, 3]), (False, [1, 1, 1, 2], [1]), (False, [1, 1, 1, 2, 3, 3, 3], [1, 3])])
@pytest.mark.parametrize('dt', list(np.typecodes['AllInteger'] + np.typecodes['Float']))
def test_mode_numerical(self, dropna, data, expected, dt):
    s = Series(data, dtype=dt)
    result = s.mode(dropna)
    expected = Series(expected, dtype=dt)
    tm.assert_series_equal(result, expected)