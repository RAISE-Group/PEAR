def test_kind(self, dtype):
    valid = set('biufcmMOSUV')
    assert dtype.kind in valid