def test_get_value(self):
    p0 = pd.Period('2017-09-01')
    p1 = pd.Period('2017-09-02')
    p2 = pd.Period('2017-09-03')
    idx0 = pd.PeriodIndex([p0, p1, p2])
    input0 = np.array([1, 2, 3])
    expected0 = 2
    result0 = idx0.get_value(input0, p1)
    assert result0 == expected0
    idx1 = pd.PeriodIndex([p1, p1, p2])
    input1 = np.array([1, 2, 3])
    expected1 = np.array([1, 2])
    result1 = idx1.get_value(input1, p1)
    tm.assert_numpy_array_equal(result1, expected1)
    idx2 = pd.PeriodIndex([p1, p2, p1])
    input2 = np.array([1, 2, 3])
    expected2 = np.array([1, 3])
    result2 = idx2.get_value(input2, p1)
    tm.assert_numpy_array_equal(result2, expected2)