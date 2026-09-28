@pytest.mark.parametrize('other', [list(range(10)), np.arange(10), np.arange(10).astype(np.float32), np.arange(10).astype(object), pd.timedelta_range('1ns', periods=10).array, np.array(pd.timedelta_range('1ns', periods=10)), list(pd.timedelta_range('1ns', periods=10)), pd.timedelta_range('1 Day', periods=10).astype(object), pd.period_range('1971-01-01', freq='D', periods=10).array, pd.period_range('1971-01-01', freq='D', periods=10).astype(object)])
def test_dt64arr_cmp_arraylike_invalid(self, other, tz_naive_fixture):
    tz = tz_naive_fixture
    dta = date_range('1970-01-01', freq='ns', periods=10, tz=tz)._data
    assert_invalid_comparison(dta, other, tm.to_array)