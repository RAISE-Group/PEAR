def test_validate_bool_args(self):
    invalid_values = [1, 'True', [1, 2, 3], 5.0]
    for value in invalid_values:
        with pytest.raises(ValueError):
            self.int_series.drop_duplicates(inplace=value)