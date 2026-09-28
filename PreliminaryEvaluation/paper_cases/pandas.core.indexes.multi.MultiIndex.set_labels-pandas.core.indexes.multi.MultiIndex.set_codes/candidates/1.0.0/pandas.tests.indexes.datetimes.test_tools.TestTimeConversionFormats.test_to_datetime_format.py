@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_format(self, cache):
    values = ['1/1/2000', '1/2/2000', '1/3/2000']
    results1 = [Timestamp('20000101'), Timestamp('20000201'), Timestamp('20000301')]
    results2 = [Timestamp('20000101'), Timestamp('20000102'), Timestamp('20000103')]
    for vals, expecteds in [(values, (Index(results1), Index(results2))), (Series(values), (Series(results1), Series(results2))), (values[0], (results1[0], results2[0])), (values[1], (results1[1], results2[1])), (values[2], (results1[2], results2[2]))]:
        for i, fmt in enumerate(['%d/%m/%Y', '%m/%d/%Y']):
            result = to_datetime(vals, format=fmt, cache=cache)
            expected = expecteds[i]
            if isinstance(expected, Series):
                tm.assert_series_equal(result, Series(expected))
            elif isinstance(expected, Timestamp):
                assert result == expected
            else:
                tm.assert_index_equal(result, expected)