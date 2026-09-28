def test_pickle_compat_construction(self):
    msg = "Index\\(\\.\\.\\.\\) must be called with a collection of some kind, None was passed|__new__\\(\\) missing 1 required positional argument: 'data'|__new__\\(\\) takes at least 2 arguments \\(1 given\\)"
    with pytest.raises(TypeError, match=msg):
        self._holder()