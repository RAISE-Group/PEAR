def test_comparisons_nat(self):
    tdidx1 = pd.TimedeltaIndex(['1 day', pd.NaT, '1 day 00:00:01', pd.NaT, '1 day 00:00:01', '5 day 00:00:03'])
    tdidx2 = pd.TimedeltaIndex(['2 day', '2 day', pd.NaT, pd.NaT, '1 day 00:00:02', '5 days 00:00:03'])
    tdarr = np.array([np.timedelta64(2, 'D'), np.timedelta64(2, 'D'), np.timedelta64('nat'), np.timedelta64('nat'), np.timedelta64(1, 'D') + np.timedelta64(2, 's'), np.timedelta64(5, 'D') + np.timedelta64(3, 's')])
    cases = [(tdidx1, tdidx2), (tdidx1, tdarr)]
    for idx1, idx2 in cases:
        result = idx1 < idx2
        expected = np.array([True, False, False, False, True, False])
        tm.assert_numpy_array_equal(result, expected)
        result = idx2 > idx1
        expected = np.array([True, False, False, False, True, False])
        tm.assert_numpy_array_equal(result, expected)
        result = idx1 <= idx2
        expected = np.array([True, False, False, False, True, True])
        tm.assert_numpy_array_equal(result, expected)
        result = idx2 >= idx1
        expected = np.array([True, False, False, False, True, True])
        tm.assert_numpy_array_equal(result, expected)
        result = idx1 == idx2
        expected = np.array([False, False, False, False, False, True])
        tm.assert_numpy_array_equal(result, expected)
        result = idx1 != idx2
        expected = np.array([True, True, True, True, True, False])
        tm.assert_numpy_array_equal(result, expected)