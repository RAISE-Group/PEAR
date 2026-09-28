def test_td64arr_mul_tdlike_scalar_raises(self, two_hours, box_with_array):
    rng = timedelta_range('1 days', '10 days', name='foo')
    rng = tm.box_expected(rng, box_with_array)
    with pytest.raises(TypeError):
        rng * two_hours