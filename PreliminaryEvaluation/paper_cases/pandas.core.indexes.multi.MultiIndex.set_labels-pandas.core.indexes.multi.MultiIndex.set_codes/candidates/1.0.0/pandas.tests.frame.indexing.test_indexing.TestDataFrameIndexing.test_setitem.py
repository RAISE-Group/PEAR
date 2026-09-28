def test_setitem(self, float_frame):
    series = float_frame['A'][::2]
    float_frame['col5'] = series
    assert 'col5' in float_frame
    assert len(series) == 15
    assert len(float_frame) == 30
    exp = np.ravel(np.column_stack((series.values, [np.nan] * 15)))
    exp = Series(exp, index=float_frame.index, name='col5')
    tm.assert_series_equal(float_frame['col5'], exp)
    series = float_frame['A']
    float_frame['col6'] = series
    tm.assert_series_equal(series, float_frame['col6'], check_names=False)
    msg = '\\"None of \\[Float64Index\\(\\[.*dtype=\'float64\'\\)\\] are in the \\[columns\\]\\"'
    with pytest.raises(KeyError, match=msg):
        float_frame[np.random.randn(len(float_frame) + 1)] = 1
    arr = np.random.randn(len(float_frame))
    float_frame['col9'] = arr
    assert (float_frame['col9'] == arr).all()
    float_frame['col7'] = 5
    assert (float_frame['col7'] == 5).all()
    float_frame['col0'] = 3.14
    assert (float_frame['col0'] == 3.14).all()
    float_frame['col8'] = 'foo'
    assert (float_frame['col8'] == 'foo').all()
    smaller = float_frame[:2]
    with pytest.raises(com.SettingWithCopyError):
        smaller['col10'] = ['1', '2']
    assert smaller['col10'].dtype == np.object_
    assert (smaller['col10'] == ['1', '2']).all()
    df = DataFrame([[0, 0]])
    df.iloc[0] = np.nan
    expected = DataFrame([[np.nan, np.nan]])
    tm.assert_frame_equal(df, expected)
    df = DataFrame([[0, 0]])
    df.loc[0] = np.nan
    tm.assert_frame_equal(df, expected)