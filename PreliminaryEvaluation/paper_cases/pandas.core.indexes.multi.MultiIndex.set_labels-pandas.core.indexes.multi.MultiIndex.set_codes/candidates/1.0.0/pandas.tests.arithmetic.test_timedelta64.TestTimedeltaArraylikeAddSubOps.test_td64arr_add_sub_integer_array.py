def test_td64arr_add_sub_integer_array(self, box_with_array):
    rng = timedelta_range('1 days 09:00:00', freq='H', periods=3)
    tdarr = tm.box_expected(rng, box_with_array)
    other = tm.box_expected([4, 3, 2], box_with_array)
    msg = 'Addition/subtraction of integers and integer-arrays'
    assert_invalid_addsub_type(tdarr, other, msg)