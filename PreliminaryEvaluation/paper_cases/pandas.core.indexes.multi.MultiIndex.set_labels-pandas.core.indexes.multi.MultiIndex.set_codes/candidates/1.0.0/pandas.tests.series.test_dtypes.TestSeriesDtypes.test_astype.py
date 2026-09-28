@pytest.mark.parametrize('dtype', ['float32', 'float64', 'int64', 'int32'])
def test_astype(self, dtype):
    s = Series(np.random.randn(5), name='foo')
    as_typed = s.astype(dtype)
    assert as_typed.dtype == dtype
    assert as_typed.name == s.name