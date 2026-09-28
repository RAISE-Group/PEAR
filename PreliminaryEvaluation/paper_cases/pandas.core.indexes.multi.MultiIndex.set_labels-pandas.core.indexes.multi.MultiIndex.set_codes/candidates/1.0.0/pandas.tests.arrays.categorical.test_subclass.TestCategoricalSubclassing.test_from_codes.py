def test_from_codes(self):
    sc = tm.SubclassedCategorical.from_codes([1, 0, 2], ['a', 'b', 'c'])
    assert isinstance(sc, tm.SubclassedCategorical)
    exp = Categorical.from_codes([1, 0, 2], ['a', 'b', 'c'])
    tm.assert_categorical_equal(sc, exp)