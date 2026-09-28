@pytest.mark.parametrize('dtype,expected', [(True, Series(['2000-01-01'], dtype='datetime64[ns]')), (False, Series([946684800000]))])
def test_series_with_dtype_datetime(self, dtype, expected):
    s = Series(['2000-01-01'], dtype='datetime64[ns]')
    data = s.to_json()
    result = pd.read_json(data, typ='series', dtype=dtype)
    tm.assert_series_equal(result, expected)