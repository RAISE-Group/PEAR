def test_dt64arr_add_timestamp_raises(self, box_with_array):
    idx = DatetimeIndex(['2011-01-01', '2011-01-02'])
    idx = tm.box_expected(idx, box_with_array)
    msg = 'cannot add'
    with pytest.raises(TypeError, match=msg):
        idx + Timestamp('2011-01-01')
    with pytest.raises(TypeError, match=msg):
        Timestamp('2011-01-01') + idx