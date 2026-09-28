@pytest.mark.parametrize('freq', ['M', '2M', '3M'])
def test_pi_cmp_nat(self, freq):
    idx1 = PeriodIndex(['2011-01', '2011-02', 'NaT', '2011-05'], freq=freq)
    result = idx1 > Period('2011-02', freq=freq)
    exp = np.array([False, False, False, True])
    tm.assert_numpy_array_equal(result, exp)
    result = Period('2011-02', freq=freq) < idx1
    tm.assert_numpy_array_equal(result, exp)
    result = idx1 == Period('NaT', freq=freq)
    exp = np.array([False, False, False, False])
    tm.assert_numpy_array_equal(result, exp)
    result = Period('NaT', freq=freq) == idx1
    tm.assert_numpy_array_equal(result, exp)
    result = idx1 != Period('NaT', freq=freq)
    exp = np.array([True, True, True, True])
    tm.assert_numpy_array_equal(result, exp)
    result = Period('NaT', freq=freq) != idx1
    tm.assert_numpy_array_equal(result, exp)
    idx2 = PeriodIndex(['2011-02', '2011-01', '2011-04', 'NaT'], freq=freq)
    result = idx1 < idx2
    exp = np.array([True, False, False, False])
    tm.assert_numpy_array_equal(result, exp)
    result = idx1 == idx2
    exp = np.array([False, False, False, False])
    tm.assert_numpy_array_equal(result, exp)
    result = idx1 != idx2
    exp = np.array([True, True, True, True])
    tm.assert_numpy_array_equal(result, exp)
    result = idx1 == idx1
    exp = np.array([True, True, False, True])
    tm.assert_numpy_array_equal(result, exp)
    result = idx1 != idx1
    exp = np.array([False, False, True, False])
    tm.assert_numpy_array_equal(result, exp)