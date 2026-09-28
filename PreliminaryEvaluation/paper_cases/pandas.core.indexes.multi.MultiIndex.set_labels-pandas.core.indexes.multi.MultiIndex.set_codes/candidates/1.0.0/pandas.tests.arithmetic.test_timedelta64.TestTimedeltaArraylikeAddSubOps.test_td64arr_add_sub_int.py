def test_td64arr_add_sub_int(self, box_with_array, one):
    rng = timedelta_range('1 days 09:00:00', freq='H', periods=10)
    tdarr = tm.box_expected(rng, box_with_array)
    msg = 'Addition/subtraction of integers'
    assert_invalid_addsub_type(tdarr, one, msg)
    with pytest.raises(TypeError, match=msg):
        tdarr += one
    with pytest.raises(TypeError, match=msg):
        tdarr -= one