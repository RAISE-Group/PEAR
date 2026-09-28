def test_properties(self, interval):
    assert interval.closed == 'right'
    assert interval.left == 0
    assert interval.right == 1
    assert interval.mid == 0.5