def test_keys(self, float_frame):
    getkeys = float_frame.keys
    assert getkeys() is float_frame.columns