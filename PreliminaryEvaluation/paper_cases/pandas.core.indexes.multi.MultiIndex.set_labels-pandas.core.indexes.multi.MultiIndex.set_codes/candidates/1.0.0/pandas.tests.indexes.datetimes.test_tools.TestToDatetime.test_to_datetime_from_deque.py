def test_to_datetime_from_deque(self):
    result = pd.to_datetime(deque([pd.Timestamp('2010-06-02 09:30:00')] * 51))
    expected = pd.to_datetime([pd.Timestamp('2010-06-02 09:30:00')] * 51)
    tm.assert_index_equal(result, expected)