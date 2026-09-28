def test_mul(self):
    assert DateOffset(2) == 2 * DateOffset(1)
    assert DateOffset(2) == DateOffset(1) * 2