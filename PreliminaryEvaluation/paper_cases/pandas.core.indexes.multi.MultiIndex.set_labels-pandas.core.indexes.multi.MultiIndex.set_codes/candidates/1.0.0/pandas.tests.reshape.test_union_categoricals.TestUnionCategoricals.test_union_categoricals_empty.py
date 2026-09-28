def test_union_categoricals_empty(self):
    res = union_categoricals([pd.Categorical([]), pd.Categorical([])])
    exp = Categorical([])
    tm.assert_categorical_equal(res, exp)
    res = union_categoricals([Categorical([]), Categorical(['1'])])
    exp = Categorical(['1'])
    tm.assert_categorical_equal(res, exp)