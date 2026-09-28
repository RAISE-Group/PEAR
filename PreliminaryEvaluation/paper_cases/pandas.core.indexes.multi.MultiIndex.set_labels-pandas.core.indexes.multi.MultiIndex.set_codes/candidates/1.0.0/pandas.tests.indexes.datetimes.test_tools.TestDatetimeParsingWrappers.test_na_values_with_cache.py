@pytest.mark.parametrize('cache', [True, False])
def test_na_values_with_cache(self, cache, unique_nulls_fixture, unique_nulls_fixture2):
    expected = Index([NaT, NaT], dtype='datetime64[ns]')
    result = to_datetime([unique_nulls_fixture, unique_nulls_fixture2], cache=cache)
    tm.assert_index_equal(result, expected)