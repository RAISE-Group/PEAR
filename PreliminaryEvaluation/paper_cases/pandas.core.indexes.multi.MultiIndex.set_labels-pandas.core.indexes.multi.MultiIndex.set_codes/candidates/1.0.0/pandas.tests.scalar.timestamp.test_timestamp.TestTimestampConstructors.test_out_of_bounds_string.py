def test_out_of_bounds_string(self):
    with pytest.raises(ValueError):
        Timestamp('1676-01-01')
    with pytest.raises(ValueError):
        Timestamp('2263-01-01')