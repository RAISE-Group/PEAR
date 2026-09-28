def test_array_interface(self, data):
    if data.tz:
        pytest.skip('GH-23569')
    else:
        super().test_array_interface(data)