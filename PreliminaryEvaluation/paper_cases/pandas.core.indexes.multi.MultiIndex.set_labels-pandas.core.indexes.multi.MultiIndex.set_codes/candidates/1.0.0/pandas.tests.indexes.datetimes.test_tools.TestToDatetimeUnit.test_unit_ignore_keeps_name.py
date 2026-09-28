@pytest.mark.parametrize('cache', [True, False])
def test_unit_ignore_keeps_name(self, cache):
    expected = pd.Index([15000000000.0] * 2, name='name')
    result = pd.to_datetime(expected, errors='ignore', unit='s', cache=cache)
    tm.assert_index_equal(result, expected)