@pytest.mark.parametrize('first, expected', [[[None], 'mixed'], [[np.nan], 'mixed'], [[pd.NaT], 'nat'], [[datetime(2017, 6, 12, 19, 30), pd.NaT], 'datetime'], [[np.datetime64('2017-06-12'), pd.NaT], 'datetime'], [[date(2017, 6, 12), pd.NaT], 'date'], [[timedelta(2017, 6, 12), pd.NaT], 'timedelta'], [[np.timedelta64(2017, 'D'), pd.NaT], 'timedelta']])
@pytest.mark.parametrize('second', [None, np.nan])
def test_infer_datetimelike_array_nan_nat_like(self, first, second, expected):
    first.append(second)
    assert lib.infer_datetimelike_array(first) == expected