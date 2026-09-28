def test_cat_accessor(self):
    s = Series(Categorical(['a', 'b', np.nan, 'a']))
    tm.assert_index_equal(s.cat.categories, Index(['a', 'b']))
    assert not s.cat.ordered, False
    exp = Categorical(['a', 'b', np.nan, 'a'], categories=['b', 'a'])
    s.cat.set_categories(['b', 'a'], inplace=True)
    tm.assert_categorical_equal(s.values, exp)
    res = s.cat.set_categories(['b', 'a'])
    tm.assert_categorical_equal(res.values, exp)
    s[:] = 'a'
    s = s.cat.remove_unused_categories()
    tm.assert_index_equal(s.cat.categories, Index(['a']))