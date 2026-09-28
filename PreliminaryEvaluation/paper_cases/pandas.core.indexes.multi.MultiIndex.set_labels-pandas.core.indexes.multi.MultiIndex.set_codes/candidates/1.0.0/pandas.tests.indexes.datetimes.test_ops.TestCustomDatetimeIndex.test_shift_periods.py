def test_shift_periods(self):
    idx = pd.date_range(start=START, end=END, periods=3)
    tm.assert_index_equal(idx.shift(periods=0), idx)
    tm.assert_index_equal(idx.shift(0), idx)