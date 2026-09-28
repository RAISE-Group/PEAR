@pytest.mark.parametrize('cache', [True, False])
def test_parse_nanoseconds_with_formula(self, cache):
    for v in ['2012-01-01 09:00:00.000000001', '2012-01-01 09:00:00.000001', '2012-01-01 09:00:00.001', '2012-01-01 09:00:00.001000', '2012-01-01 09:00:00.001000000']:
        expected = pd.to_datetime(v, cache=cache)
        result = pd.to_datetime(v, format='%Y-%m-%d %H:%M:%S.%f', cache=cache)
        assert result == expected