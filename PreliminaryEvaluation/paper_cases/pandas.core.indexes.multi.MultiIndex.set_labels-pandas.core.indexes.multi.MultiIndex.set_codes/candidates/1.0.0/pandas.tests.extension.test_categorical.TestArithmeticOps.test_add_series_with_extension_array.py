def test_add_series_with_extension_array(self, data):
    ser = pd.Series(data)
    with pytest.raises(TypeError, match='cannot perform|unsupported operand'):
        ser + data