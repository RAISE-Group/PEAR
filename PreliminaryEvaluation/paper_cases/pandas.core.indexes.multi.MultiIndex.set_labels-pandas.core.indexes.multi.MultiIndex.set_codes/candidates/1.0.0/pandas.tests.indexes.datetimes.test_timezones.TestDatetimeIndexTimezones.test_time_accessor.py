@pytest.mark.parametrize('dtype', [None, 'datetime64[ns, CET]', 'datetime64[ns, EST]', 'datetime64[ns, UTC]'])
def test_time_accessor(self, dtype):
    expected = np.array([time(10, 20, 30), pd.NaT])
    index = DatetimeIndex(['2018-06-04 10:20:30', pd.NaT], dtype=dtype)
    result = index.time
    tm.assert_numpy_array_equal(result, expected)