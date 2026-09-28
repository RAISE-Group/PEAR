def test_is_copy(self, date_range_frame):
    df = date_range_frame
    N = 50
    df.loc[15:30, 'A'] = np.nan
    dates = date_range('1/1/1990', periods=N * 3, freq='25s')
    result = df.asof(dates)
    with tm.assert_produces_warning(None):
        result['C'] = 1