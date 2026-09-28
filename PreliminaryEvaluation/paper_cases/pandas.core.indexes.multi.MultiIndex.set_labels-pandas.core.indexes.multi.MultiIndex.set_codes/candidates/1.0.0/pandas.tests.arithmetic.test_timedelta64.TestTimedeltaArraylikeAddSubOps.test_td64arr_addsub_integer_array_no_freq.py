def test_td64arr_addsub_integer_array_no_freq(self, box_with_array):
    tdi = TimedeltaIndex(['1 Day', 'NaT', '3 Hours'])
    tdarr = tm.box_expected(tdi, box_with_array)
    other = tm.box_expected([14, -1, 16], box_with_array)
    msg = 'Addition/subtraction of integers'
    assert_invalid_addsub_type(tdarr, other, msg)