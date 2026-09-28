def test_min_max_categorical(self):
    ci = pd.CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=False)
    with pytest.raises(TypeError):
        ci.min()
    with pytest.raises(TypeError):
        ci.max()
    ci = pd.CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=True)
    assert ci.min() == 'c'
    assert ci.max() == 'b'