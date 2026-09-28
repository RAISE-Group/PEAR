@pytest.mark.parametrize('tuples, closed, expected_data', [([(0, 1), (1, 2), (2, 3)], 'left', ['[0, 1)', '[1, 2)', '[2, 3)']), ([(0.5, 1.0), np.nan, (2.0, 3.0)], 'right', ['(0.5, 1.0]', 'NaN', '(2.0, 3.0]']), ([(Timestamp('20180101'), Timestamp('20180102')), np.nan, (Timestamp('20180102'), Timestamp('20180103'))], 'both', ['[2018-01-01, 2018-01-02]', 'NaN', '[2018-01-02, 2018-01-03]']), ([(Timedelta('0 days'), Timedelta('1 days')), (Timedelta('1 days'), Timedelta('2 days')), np.nan], 'neither', ['(0 days 00:00:00, 1 days 00:00:00)', '(1 days 00:00:00, 2 days 00:00:00)', 'NaN'])])
def test_to_native_types(self, tuples, closed, expected_data):
    index = IntervalIndex.from_tuples(tuples, closed=closed)
    result = index.to_native_types()
    expected = np.array(expected_data)
    tm.assert_numpy_array_equal(result, expected)