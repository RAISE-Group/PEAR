def test_contains(self):
    ci = self.create_index(categories=list('cabdef'))
    assert 'a' in ci
    assert 'z' not in ci
    assert 'e' not in ci
    assert np.nan not in ci
    assert 0 not in ci
    assert 1 not in ci
    ci = CategoricalIndex(list('aabbca') + [np.nan], categories=list('cabdef'))
    assert np.nan in ci