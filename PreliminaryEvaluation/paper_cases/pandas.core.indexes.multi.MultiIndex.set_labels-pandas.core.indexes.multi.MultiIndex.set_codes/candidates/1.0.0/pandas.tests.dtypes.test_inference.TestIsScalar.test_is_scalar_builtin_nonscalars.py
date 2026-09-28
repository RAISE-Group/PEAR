def test_is_scalar_builtin_nonscalars(self):
    assert not is_scalar({})
    assert not is_scalar([])
    assert not is_scalar([1])
    assert not is_scalar(())
    assert not is_scalar((1,))
    assert not is_scalar(slice(None))
    assert not is_scalar(Ellipsis)