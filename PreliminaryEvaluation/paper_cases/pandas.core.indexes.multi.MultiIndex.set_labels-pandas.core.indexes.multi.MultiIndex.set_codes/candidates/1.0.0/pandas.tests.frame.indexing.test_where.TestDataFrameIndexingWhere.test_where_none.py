def test_where_none(self):
    df = DataFrame({'series': Series(range(10))}).astype(float)
    df[df > 7] = None
    expected = DataFrame({'series': Series([0, 1, 2, 3, 4, 5, 6, 7, np.nan, np.nan])})
    tm.assert_frame_equal(df, expected)
    df = DataFrame([{'A': 1, 'B': np.nan, 'C': 'Test'}, {'A': np.nan, 'B': 'Test', 'C': np.nan}])
    msg = 'boolean setting on mixed-type'
    with pytest.raises(TypeError, match=msg):
        df.where(~isna(df), None, inplace=True)