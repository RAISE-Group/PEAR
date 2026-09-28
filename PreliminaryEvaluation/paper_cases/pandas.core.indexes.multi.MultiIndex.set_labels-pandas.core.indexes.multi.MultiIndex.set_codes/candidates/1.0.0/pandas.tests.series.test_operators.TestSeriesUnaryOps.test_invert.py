def test_invert(self):
    ser = tm.makeStringSeries()
    ser.name = 'series'
    tm.assert_series_equal(-(ser < 0), ~(ser < 0))