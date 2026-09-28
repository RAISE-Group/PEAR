def test_datetime64_with_index(self):
    ser = pd.Series(np.random.randn(5))
    expected = ser - ser.index.to_series()
    result = ser - ser.index
    tm.assert_series_equal(result, expected)
    ser = pd.Series(pd.date_range('20130101', periods=5), index=pd.date_range('20130101', periods=5))
    expected = ser - ser.index.to_series()
    result = ser - ser.index
    tm.assert_series_equal(result, expected)
    with pytest.raises(TypeError):
        result = ser - ser.index.to_period()
    df = pd.DataFrame(np.random.randn(5, 2), index=pd.date_range('20130101', periods=5))
    df['date'] = pd.Timestamp('20130102')
    df['expected'] = df['date'] - df.index.to_series()
    df['result'] = df['date'] - df.index
    tm.assert_series_equal(df['result'], df['expected'], check_names=False)