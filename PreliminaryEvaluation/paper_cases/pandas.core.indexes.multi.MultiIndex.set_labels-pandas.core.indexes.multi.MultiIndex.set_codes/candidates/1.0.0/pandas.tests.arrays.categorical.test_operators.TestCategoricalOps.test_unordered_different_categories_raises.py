def test_unordered_different_categories_raises(self):
    c1 = Categorical(['a', 'b'], categories=['a', 'b'], ordered=False)
    c2 = Categorical(['a', 'c'], categories=['c', 'a'], ordered=False)
    with pytest.raises(TypeError, match='Categoricals can only be compared'):
        c1 == c2