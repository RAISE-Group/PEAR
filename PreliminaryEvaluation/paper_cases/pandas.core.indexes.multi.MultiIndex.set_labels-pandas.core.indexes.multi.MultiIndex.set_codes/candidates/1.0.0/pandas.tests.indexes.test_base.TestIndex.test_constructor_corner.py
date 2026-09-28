def test_constructor_corner(self):
    msg = 'Index\\(\\.\\.\\.\\) must be called with a collection of some kind, 0 was passed'
    with pytest.raises(TypeError, match=msg):
        Index(0)