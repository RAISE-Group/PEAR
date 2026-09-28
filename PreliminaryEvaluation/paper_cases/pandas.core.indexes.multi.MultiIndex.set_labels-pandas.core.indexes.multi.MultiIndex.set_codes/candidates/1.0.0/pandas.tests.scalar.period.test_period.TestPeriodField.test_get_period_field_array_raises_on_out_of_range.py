def test_get_period_field_array_raises_on_out_of_range(self):
    msg = "Buffer dtype mismatch, expected 'int64_t' but got 'double'"
    with pytest.raises(ValueError, match=msg):
        libperiod.get_period_field_arr(-1, np.empty(1), 0)