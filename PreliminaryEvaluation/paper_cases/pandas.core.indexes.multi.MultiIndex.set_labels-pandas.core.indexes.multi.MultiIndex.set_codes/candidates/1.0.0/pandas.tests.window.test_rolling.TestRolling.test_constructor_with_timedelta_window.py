@pytest.mark.parametrize('window', [timedelta(days=3), pd.Timedelta(days=3)])
def test_constructor_with_timedelta_window(self, window):
    n = 10
    df = DataFrame({'value': np.arange(n)}, index=pd.date_range('2015-12-24', periods=n, freq='D'))
    expected_data = np.append([0.0, 1.0], np.arange(3.0, 27.0, 3))
    result = df.rolling(window=window).sum()
    expected = DataFrame({'value': expected_data}, index=pd.date_range('2015-12-24', periods=n, freq='D'))
    tm.assert_frame_equal(result, expected)
    expected = df.rolling('3D').sum()
    tm.assert_frame_equal(result, expected)