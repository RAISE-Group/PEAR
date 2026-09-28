def test_take_nd_deprecated(self):
    cat = pd.Categorical(['a', 'b', 'c'])
    with tm.assert_produces_warning(FutureWarning):
        cat.take_nd([0, 1])
    ci = pd.Index(cat)
    with tm.assert_produces_warning(FutureWarning):
        ci.take_nd([0, 1])