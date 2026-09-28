def test_ndarray_compat_properties(self):
    for o in self.objs:
        for p in ['shape', 'dtype', 'T', 'nbytes']:
            assert getattr(o, p, None) is not None
        for p in ['flags', 'strides', 'itemsize', 'base', 'data']:
            assert not hasattr(o, p)
        with pytest.raises(ValueError):
            o.item()
        assert o.ndim == 1
        assert o.size == len(o)
    assert Index([1]).item() == 1
    assert Series([1]).item() == 1