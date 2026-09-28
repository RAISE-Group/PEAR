@pytest.mark.parametrize('offset,utc,exp', [['Z', True, '2019-01-01T00:00:00.000Z'], ['Z', None, '2019-01-01T00:00:00.000Z'], ['-01:00', True, '2019-01-01T01:00:00.000Z'], ['-01:00', None, '2019-01-01T00:00:00.000-01:00']])
def test_arg_tz_ns_unit(self, offset, utc, exp):
    arg = '2019-01-01T00:00:00.000' + offset
    result = to_datetime([arg], unit='ns', utc=utc)
    expected = to_datetime([exp])
    tm.assert_index_equal(result, expected)