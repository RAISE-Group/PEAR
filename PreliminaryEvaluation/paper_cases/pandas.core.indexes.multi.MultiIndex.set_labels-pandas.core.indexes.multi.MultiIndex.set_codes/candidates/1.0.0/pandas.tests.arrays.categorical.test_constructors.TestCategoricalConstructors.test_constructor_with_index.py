def test_constructor_with_index(self):
    ci = CategoricalIndex(list('aabbca'), categories=list('cab'))
    tm.assert_categorical_equal(ci.values, Categorical(ci))
    ci = CategoricalIndex(list('aabbca'), categories=list('cab'))
    tm.assert_categorical_equal(ci.values, Categorical(ci.astype(object), categories=ci.categories))