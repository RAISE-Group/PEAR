def test_barely_out_of_bounds(self):
    with pytest.raises(OutOfBoundsDatetime):
        Timestamp('2262-04-11 23:47:16.854775808')