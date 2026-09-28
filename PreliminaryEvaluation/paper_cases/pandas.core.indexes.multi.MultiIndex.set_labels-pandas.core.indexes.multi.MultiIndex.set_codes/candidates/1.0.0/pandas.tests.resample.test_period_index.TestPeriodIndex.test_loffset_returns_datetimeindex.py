@pytest.mark.parametrize('kind', ['period', None, 'timestamp'])
@pytest.mark.parametrize('agg_arg', ['mean', {'value': 'mean'}, ['mean']])
def test_loffset_returns_datetimeindex(self, frame, kind, agg_arg):
    df = frame
    expected_means = [df.values[i:i + 2].mean() for i in range(0, len(df.values), 2)]
    expected_index = period_range(df.index[0], periods=len(df.index) / 2, freq='2D')
    expected_index = expected_index.to_timestamp()
    expected_index += timedelta(hours=2)
    expected = DataFrame({'value': expected_means}, index=expected_index)
    result_agg = df.resample('2D', loffset='2H', kind=kind).agg(agg_arg)
    if isinstance(agg_arg, list):
        expected.columns = pd.MultiIndex.from_tuples([('value', 'mean')])
    tm.assert_frame_equal(result_agg, expected)