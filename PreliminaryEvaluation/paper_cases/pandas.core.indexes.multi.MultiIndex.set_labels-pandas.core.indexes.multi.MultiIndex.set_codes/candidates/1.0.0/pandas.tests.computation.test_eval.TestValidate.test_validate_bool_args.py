def test_validate_bool_args(self):
    invalid_values = [1, 'True', [1, 2, 3], 5.0]
    for value in invalid_values:
        with pytest.raises(ValueError):
            pd.eval('2+2', inplace=value)