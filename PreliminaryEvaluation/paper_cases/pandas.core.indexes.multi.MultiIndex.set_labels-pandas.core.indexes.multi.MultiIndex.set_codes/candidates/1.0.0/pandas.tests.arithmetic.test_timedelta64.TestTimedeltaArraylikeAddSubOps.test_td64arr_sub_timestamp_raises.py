def test_td64arr_sub_timestamp_raises(self, box_with_array):
    idx = TimedeltaIndex(['1 day', '2 day'])
    idx = tm.box_expected(idx, box_with_array)
    msg = 'cannot subtract a datelike from|Could not operate|cannot perform operation'
    with pytest.raises(TypeError, match=msg):
        idx - Timestamp('2011-01-01')