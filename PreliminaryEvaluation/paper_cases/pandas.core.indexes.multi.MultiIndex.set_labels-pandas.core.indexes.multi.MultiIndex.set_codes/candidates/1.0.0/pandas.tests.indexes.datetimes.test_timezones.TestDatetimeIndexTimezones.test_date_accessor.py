@pytest.mark.parametrize('dtype', [None, 'datetime64[ns, CET]', 'datetime64[ns, EST]', 'datetime64[ns, UTC]'])
def test_date_accessor(self, dtype):
    expected = np.array([date(2018, 6, 4), pd.NaT])
    index = DatetimeIndex(['2018-06-04 10:00:00', pd.NaT], dtype=dtype)
    result = index.date
    tm.assert_numpy_array_equal(result, expected)