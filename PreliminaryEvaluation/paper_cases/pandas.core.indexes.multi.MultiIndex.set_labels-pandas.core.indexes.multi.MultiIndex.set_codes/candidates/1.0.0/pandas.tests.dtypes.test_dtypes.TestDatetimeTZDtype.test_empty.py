def test_empty(self):
    with pytest.raises(TypeError, match="A 'tz' is required."):
        DatetimeTZDtype()