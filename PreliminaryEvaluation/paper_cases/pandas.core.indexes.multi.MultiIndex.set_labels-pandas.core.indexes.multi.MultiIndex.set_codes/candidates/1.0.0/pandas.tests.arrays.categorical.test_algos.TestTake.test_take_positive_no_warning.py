def test_take_positive_no_warning(self):
    cat = pd.Categorical(['a', 'b'])
    with tm.assert_produces_warning(None):
        cat.take([0, 0])