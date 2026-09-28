def test_all_any_params(self):
    s1 = Series([np.nan, True])
    s2 = Series([np.nan, False])
    assert s1.all(skipna=False)
    assert s1.all(skipna=True)
    assert np.isnan(s2.any(skipna=False))
    assert not s2.any(skipna=True)
    s = pd.Series([False, False, True, True, False, True], index=[0, 0, 1, 1, 2, 2])
    tm.assert_series_equal(s.all(level=0), Series([False, True, False]))
    tm.assert_series_equal(s.any(level=0), Series([False, True, True]))
    with pytest.raises(NotImplementedError):
        s.any(bool_only=True, level=0)
    with pytest.raises(NotImplementedError):
        s.all(bool_only=True, level=0)
    with pytest.raises(NotImplementedError):
        s.any(bool_only=True)
    with pytest.raises(NotImplementedError):
        s.all(bool_only=True)