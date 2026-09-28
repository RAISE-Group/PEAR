def test_constructor(self):
    sc = tm.SubclassedCategorical(['a', 'b', 'c'])
    assert isinstance(sc, tm.SubclassedCategorical)
    tm.assert_categorical_equal(sc, Categorical(['a', 'b', 'c']))