def test_bday_near_overflow(self):
    start = pd.Timestamp.max.floor('D').to_pydatetime()
    rng = pd.date_range(start, end=None, periods=1, freq='B')
    expected = pd.DatetimeIndex([start], freq='B')
    tm.assert_index_equal(rng, expected)