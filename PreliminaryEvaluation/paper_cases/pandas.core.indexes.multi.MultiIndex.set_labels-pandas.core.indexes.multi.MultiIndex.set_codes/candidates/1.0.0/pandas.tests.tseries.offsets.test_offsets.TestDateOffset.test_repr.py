def test_repr(self):
    repr(DateOffset())
    repr(DateOffset(2))
    repr(2 * DateOffset())
    repr(2 * DateOffset(months=2))