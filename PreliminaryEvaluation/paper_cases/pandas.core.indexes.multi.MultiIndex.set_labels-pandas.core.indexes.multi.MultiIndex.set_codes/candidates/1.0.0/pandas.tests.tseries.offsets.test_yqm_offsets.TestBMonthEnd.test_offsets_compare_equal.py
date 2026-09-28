def test_offsets_compare_equal(self):
    offset1 = BMonthEnd()
    offset2 = BMonthEnd()
    assert not offset1 != offset2