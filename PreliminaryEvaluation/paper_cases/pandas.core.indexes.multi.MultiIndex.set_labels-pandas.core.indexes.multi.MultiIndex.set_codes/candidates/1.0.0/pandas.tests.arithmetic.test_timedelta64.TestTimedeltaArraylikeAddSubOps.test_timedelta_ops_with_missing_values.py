def test_timedelta_ops_with_missing_values(self):
    s1 = pd.to_timedelta(Series(['00:00:01']))
    s2 = pd.to_timedelta(Series(['00:00:02']))
    msg = 'dtype datetime64\\[ns\\] cannot be converted to timedelta64\\[ns\\]'
    with pytest.raises(TypeError, match=msg):
        pd.to_timedelta(Series([pd.NaT]))
    sn = pd.to_timedelta(Series([pd.NaT], dtype='m8[ns]'))
    df1 = pd.DataFrame(['00:00:01']).apply(pd.to_timedelta)
    df2 = pd.DataFrame(['00:00:02']).apply(pd.to_timedelta)
    with pytest.raises(TypeError, match=msg):
        pd.DataFrame([pd.NaT]).apply(pd.to_timedelta)
    dfn = pd.DataFrame([pd.NaT.value]).apply(pd.to_timedelta)
    scalar1 = pd.to_timedelta('00:00:01')
    scalar2 = pd.to_timedelta('00:00:02')
    timedelta_NaT = pd.to_timedelta('NaT')
    actual = scalar1 + scalar1
    assert actual == scalar2
    actual = scalar2 - scalar1
    assert actual == scalar1
    actual = s1 + s1
    tm.assert_series_equal(actual, s2)
    actual = s2 - s1
    tm.assert_series_equal(actual, s1)
    actual = s1 + scalar1
    tm.assert_series_equal(actual, s2)
    actual = scalar1 + s1
    tm.assert_series_equal(actual, s2)
    actual = s2 - scalar1
    tm.assert_series_equal(actual, s1)
    actual = -scalar1 + s2
    tm.assert_series_equal(actual, s1)
    actual = s1 + timedelta_NaT
    tm.assert_series_equal(actual, sn)
    actual = timedelta_NaT + s1
    tm.assert_series_equal(actual, sn)
    actual = s1 - timedelta_NaT
    tm.assert_series_equal(actual, sn)
    actual = -timedelta_NaT + s1
    tm.assert_series_equal(actual, sn)
    with pytest.raises(TypeError):
        s1 + np.nan
    with pytest.raises(TypeError):
        np.nan + s1
    with pytest.raises(TypeError):
        s1 - np.nan
    with pytest.raises(TypeError):
        -np.nan + s1
    actual = s1 + pd.NaT
    tm.assert_series_equal(actual, sn)
    actual = s2 - pd.NaT
    tm.assert_series_equal(actual, sn)
    actual = s1 + df1
    tm.assert_frame_equal(actual, df2)
    actual = s2 - df1
    tm.assert_frame_equal(actual, df1)
    actual = df1 + s1
    tm.assert_frame_equal(actual, df2)
    actual = df2 - s1
    tm.assert_frame_equal(actual, df1)
    actual = df1 + df1
    tm.assert_frame_equal(actual, df2)
    actual = df2 - df1
    tm.assert_frame_equal(actual, df1)
    actual = df1 + scalar1
    tm.assert_frame_equal(actual, df2)
    actual = df2 - scalar1
    tm.assert_frame_equal(actual, df1)
    actual = df1 + timedelta_NaT
    tm.assert_frame_equal(actual, dfn)
    actual = df1 - timedelta_NaT
    tm.assert_frame_equal(actual, dfn)
    with pytest.raises(TypeError):
        df1 + np.nan
    with pytest.raises(TypeError):
        df1 - np.nan
    actual = df1 + pd.NaT
    tm.assert_frame_equal(actual, dfn)
    actual = df1 - pd.NaT
    tm.assert_frame_equal(actual, dfn)