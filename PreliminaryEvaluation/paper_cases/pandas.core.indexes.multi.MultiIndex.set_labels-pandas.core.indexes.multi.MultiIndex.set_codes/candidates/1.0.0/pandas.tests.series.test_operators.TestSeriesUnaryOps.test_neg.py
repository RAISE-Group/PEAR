def test_neg(self):
    ser = tm.makeStringSeries()
    ser.name = 'series'
    tm.assert_series_equal(-ser, -1 * ser)