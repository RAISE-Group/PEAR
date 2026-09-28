@pytest.mark.parametrize('func', ['is_datetime_array', 'is_datetime64_array', 'is_bool_array', 'is_timedelta_or_timedelta64_array', 'is_date_array', 'is_time_array', 'is_interval_array', 'is_period_array'])
def test_other_dtypes_for_array(self, func):
    func = getattr(lib, func)
    arr = np.array(['foo', 'bar'])
    assert not func(arr)
    arr = np.array([1, 2])
    assert not func(arr)