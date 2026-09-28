def test_categorical_index_repr(self):
    idx = CategoricalIndex(Categorical([1, 2, 3]))
    exp = "CategoricalIndex([1, 2, 3], categories=[1, 2, 3], ordered=False, dtype='category')"
    assert repr(idx) == exp
    i = CategoricalIndex(Categorical(np.arange(10)))
    exp = "CategoricalIndex([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], categories=[0, 1, 2, 3, 4, 5, 6, 7, ...], ordered=False, dtype='category')"
    assert repr(i) == exp