def test_add_series_with_extension_array(self, data):
    ser = pd.Series(data)
    with pytest.raises(TypeError, match='unsupported'):
        ser + data