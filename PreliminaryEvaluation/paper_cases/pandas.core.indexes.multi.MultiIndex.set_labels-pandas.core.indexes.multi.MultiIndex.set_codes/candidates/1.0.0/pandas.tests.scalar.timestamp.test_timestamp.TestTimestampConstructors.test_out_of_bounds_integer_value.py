def test_out_of_bounds_integer_value(self):
    with pytest.raises(OutOfBoundsDatetime):
        Timestamp(Timestamp.max.value * 2)
    with pytest.raises(OutOfBoundsDatetime):
        Timestamp(Timestamp.min.value * 2)