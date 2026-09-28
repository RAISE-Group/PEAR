def test_constructor_complex_dtypes(self):
    a = np.random.rand(10).astype(np.complex64)
    b = np.random.rand(10).astype(np.complex128)
    df = DataFrame({'a': a, 'b': b})
    assert a.dtype == df.a.dtype
    assert b.dtype == df.b.dtype