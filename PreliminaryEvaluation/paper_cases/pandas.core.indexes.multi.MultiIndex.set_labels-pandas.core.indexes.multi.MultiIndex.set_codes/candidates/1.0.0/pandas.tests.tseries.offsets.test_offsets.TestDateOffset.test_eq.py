def test_eq(self):
    offset1 = DateOffset(days=1)
    offset2 = DateOffset(days=365)
    assert offset1 != offset2