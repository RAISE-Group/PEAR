def test_copy(self):
    assert DateOffset(months=2).copy() == DateOffset(months=2)