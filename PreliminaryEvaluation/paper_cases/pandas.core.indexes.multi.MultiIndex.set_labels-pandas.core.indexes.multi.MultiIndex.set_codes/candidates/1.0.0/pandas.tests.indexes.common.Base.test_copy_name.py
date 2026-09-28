def test_copy_name(self, indices):
    if isinstance(indices, MultiIndex):
        return
    first = type(indices)(indices, copy=True, name='mario')
    second = type(first)(first, copy=False)
    assert first is not second
    assert indices.equals(first)
    assert first.name == 'mario'
    assert second.name == 'mario'
    s1 = Series(2, index=first)
    s2 = Series(3, index=second[:-1])
    if not isinstance(indices, CategoricalIndex):
        s3 = s1 * s2
        assert s3.index.name == 'mario'