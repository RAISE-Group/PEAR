def test_dataframe_dummies_preserve_categorical_dtype(self, dtype):
    for ordered in [False, True]:
        cat = pd.Categorical(list('xy'), categories=list('xyz'), ordered=ordered)
        result = get_dummies(cat, dtype=dtype)
        data = np.array([[1, 0, 0], [0, 1, 0]], dtype=self.effective_dtype(dtype))
        cols = pd.CategoricalIndex(cat.categories, categories=cat.categories, ordered=ordered)
        expected = DataFrame(data, columns=cols, dtype=self.effective_dtype(dtype))
        tm.assert_frame_equal(result, expected)