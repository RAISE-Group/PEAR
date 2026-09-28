def test_map_float_to_string_precision(self):
    ser = pd.Series(1 / 3)
    result = ser.map(lambda val: str(val)).to_dict()
    expected = {0: '0.3333333333333333'}
    assert result == expected