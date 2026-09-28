def test_quantile_interpolation_datetime(self, datetime_frame):
    df = datetime_frame
    q = df.quantile(0.1, axis=0, interpolation='linear')
    assert q['A'] == np.percentile(df['A'], 10)