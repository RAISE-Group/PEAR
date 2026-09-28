def test_categorical_index_repr_ordered(self):
    i = CategoricalIndex(Categorical([1, 2, 3], ordered=True))
    exp = "CategoricalIndex([1, 2, 3], categories=[1, 2, 3], ordered=True, dtype='category')"
    assert repr(i) == exp
    i = CategoricalIndex(Categorical(np.arange(10), ordered=True))
    exp = "CategoricalIndex([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], categories=[0, 1, 2, 3, 4, 5, 6, 7, ...], ordered=True, dtype='category')"
    assert repr(i) == exp