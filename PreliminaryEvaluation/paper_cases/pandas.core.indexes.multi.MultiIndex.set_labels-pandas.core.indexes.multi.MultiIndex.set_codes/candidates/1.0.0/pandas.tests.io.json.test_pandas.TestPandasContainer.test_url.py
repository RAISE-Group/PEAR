@tm.network
@pytest.mark.single
@pytest.mark.parametrize('field,dtype', [['created_at', pd.DatetimeTZDtype(tz='UTC')], ['closed_at', 'datetime64[ns]'], ['updated_at', pd.DatetimeTZDtype(tz='UTC')]])
def test_url(self, field, dtype):
    url = 'https://api.github.com/repos/pandas-dev/pandas/issues?per_page=5'
    result = read_json(url, convert_dates=True)
    assert result[field].dtype == dtype