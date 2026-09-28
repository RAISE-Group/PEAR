@pytest.mark.parametrize('copy', [True, False])
@pytest.mark.parametrize('method, tz', [['tz_localize', None], ['tz_convert', 'Europe/Berlin']])
def test_tz_localize_convert_copy_inplace_mutate(self, copy, method, tz):
    result = Series(np.arange(0, 5), index=date_range('20131027', periods=5, freq='1H', tz=tz))
    getattr(result, method)('UTC', copy=copy)
    expected = Series(np.arange(0, 5), index=date_range('20131027', periods=5, freq='1H', tz=tz))
    tm.assert_series_equal(result, expected)