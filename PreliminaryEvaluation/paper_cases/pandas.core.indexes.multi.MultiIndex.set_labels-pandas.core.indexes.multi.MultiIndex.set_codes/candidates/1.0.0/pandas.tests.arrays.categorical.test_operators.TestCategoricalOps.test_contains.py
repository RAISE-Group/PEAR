def test_contains(self):
    c = pd.Categorical(list('aabbca'), categories=list('cab'))
    assert 'b' in c
    assert 'z' not in c
    assert np.nan not in c
    with pytest.raises(TypeError, match="unhashable type: 'list'"):
        assert [1] in c
    assert 0 not in c
    assert 1 not in c
    c = pd.Categorical(list('aabbca') + [np.nan], categories=list('cab'))
    assert np.nan in c