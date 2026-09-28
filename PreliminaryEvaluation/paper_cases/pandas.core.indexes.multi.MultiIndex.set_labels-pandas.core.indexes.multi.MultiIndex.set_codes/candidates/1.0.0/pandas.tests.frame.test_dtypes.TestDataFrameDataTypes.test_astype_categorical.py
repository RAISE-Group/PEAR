@pytest.mark.parametrize('dtype', ['category', CategoricalDtype(), CategoricalDtype(ordered=True), CategoricalDtype(ordered=False), CategoricalDtype(categories=list('abcdef')), CategoricalDtype(categories=list('edba'), ordered=False), CategoricalDtype(categories=list('edcb'), ordered=True)], ids=repr)
def test_astype_categorical(self, dtype):
    d = {'A': list('abbc'), 'B': list('bccd'), 'C': list('cdde')}
    df = DataFrame(d)
    result = df.astype(dtype)
    expected = DataFrame({k: Categorical(d[k], dtype=dtype) for k in d})
    tm.assert_frame_equal(result, expected)