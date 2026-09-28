def test_get_level_number_out_of_bounds(self):
    with pytest.raises(IndexError, match='Too many levels'):
        self.frame.index._get_level_number(2)
    with pytest.raises(IndexError, match='not a valid level number'):
        self.frame.index._get_level_number(-3)