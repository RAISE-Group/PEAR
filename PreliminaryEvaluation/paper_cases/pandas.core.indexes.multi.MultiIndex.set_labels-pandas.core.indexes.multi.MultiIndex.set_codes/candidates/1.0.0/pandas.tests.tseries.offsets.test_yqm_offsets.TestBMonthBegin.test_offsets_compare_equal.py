def test_offsets_compare_equal(self):
    offset1 = BMonthBegin()
    offset2 = BMonthBegin()
    assert not offset1 != offset2