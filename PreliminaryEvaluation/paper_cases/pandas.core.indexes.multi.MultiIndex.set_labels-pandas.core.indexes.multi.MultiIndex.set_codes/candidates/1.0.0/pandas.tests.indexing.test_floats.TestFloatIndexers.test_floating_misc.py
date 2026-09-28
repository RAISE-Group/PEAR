def test_floating_misc(self):
    s = Series(np.arange(5), index=np.arange(5) * 2.5, dtype=np.int64)
    result1 = s[1.0:3.0]
    result2 = s.loc[1.0:3.0]
    result3 = s.loc[1.0:3.0]
    tm.assert_series_equal(result1, result2)
    tm.assert_series_equal(result1, result3)
    result1 = s[5.0]
    result2 = s.loc[5.0]
    result3 = s.loc[5.0]
    assert result1 == result2
    assert result1 == result3
    result1 = s[5]
    result2 = s.loc[5]
    result3 = s.loc[5]
    assert result1 == result2
    assert result1 == result3
    assert s[5.0] == s[5]
    with pytest.raises(KeyError, match='^4\\.0$'):
        s.loc[4]
    with pytest.raises(KeyError, match='^4\\.0$'):
        s.loc[4]
    with pytest.raises(KeyError, match='^4\\.0$'):
        s[4]
    expected = Series([2, 0], index=Float64Index([5.0, 0.0]))
    for fancy_idx in [[5.0, 0.0], np.array([5.0, 0.0])]:
        tm.assert_series_equal(s[fancy_idx], expected)
        tm.assert_series_equal(s.loc[fancy_idx], expected)
        tm.assert_series_equal(s.loc[fancy_idx], expected)
    expected = Series([2, 0], index=Index([5, 0], dtype='int64'))
    for fancy_idx in [[5, 0], np.array([5, 0])]:
        tm.assert_series_equal(s[fancy_idx], expected)
        tm.assert_series_equal(s.loc[fancy_idx], expected)
        tm.assert_series_equal(s.loc[fancy_idx], expected)
    result1 = s.loc[2:5]
    result2 = s.loc[2.0:5.0]
    result3 = s.loc[2.0:5]
    result4 = s.loc[2.1:5]
    tm.assert_series_equal(result1, result2)
    tm.assert_series_equal(result1, result3)
    tm.assert_series_equal(result1, result4)
    result1 = s[2:5]
    result2 = s[2.0:5.0]
    result3 = s[2.0:5]
    result4 = s[2.1:5]
    tm.assert_series_equal(result1, result2)
    tm.assert_series_equal(result1, result3)
    tm.assert_series_equal(result1, result4)
    result1 = s.loc[2:5]
    result2 = s.loc[2.0:5.0]
    result3 = s.loc[2.0:5]
    result4 = s.loc[2.1:5]
    tm.assert_series_equal(result1, result2)
    tm.assert_series_equal(result1, result3)
    tm.assert_series_equal(result1, result4)
    result1 = s.loc[2:5]
    result2 = s.loc[2:5]
    result3 = s[2:5]
    tm.assert_series_equal(result1, result2)
    tm.assert_series_equal(result1, result3)
    result1 = s[[0.0, 5, 10]]
    result2 = s.loc[[0.0, 5, 10]]
    result3 = s.loc[[0.0, 5, 10]]
    result4 = s.iloc[[0, 2, 4]]
    tm.assert_series_equal(result1, result2)
    tm.assert_series_equal(result1, result3)
    tm.assert_series_equal(result1, result4)
    with pytest.raises(KeyError, match='with any missing labels'):
        s[[1.6, 5, 10]]
    with pytest.raises(KeyError, match='with any missing labels'):
        s.loc[[1.6, 5, 10]]
    with pytest.raises(KeyError, match='with any missing labels'):
        s[[0, 1, 2]]
    with pytest.raises(KeyError, match='with any missing labels'):
        s.loc[[0, 1, 2]]
    result1 = s.loc[[2.5, 5]]
    result2 = s.loc[[2.5, 5]]
    tm.assert_series_equal(result1, result2)
    tm.assert_series_equal(result1, Series([1, 2], index=[2.5, 5.0]))
    result1 = s[[2.5]]
    result2 = s.loc[[2.5]]
    result3 = s.loc[[2.5]]
    tm.assert_series_equal(result1, result2)
    tm.assert_series_equal(result1, result3)
    tm.assert_series_equal(result1, Series([1], index=[2.5]))