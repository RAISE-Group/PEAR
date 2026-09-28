def test_categorical_delegations(self):
    msg = "Can only use \\.cat accessor with a 'category' dtype"
    with pytest.raises(AttributeError, match=msg):
        Series([1, 2, 3]).cat
    with pytest.raises(AttributeError, match=msg):
        Series([1, 2, 3]).cat()
    with pytest.raises(AttributeError, match=msg):
        Series(['a', 'b', 'c']).cat
    with pytest.raises(AttributeError, match=msg):
        Series(np.arange(5.0)).cat
    with pytest.raises(AttributeError, match=msg):
        Series([Timestamp('20130101')]).cat
    s = Series(Categorical(['a', 'b', 'c', 'a'], ordered=True))
    exp_categories = Index(['a', 'b', 'c'])
    tm.assert_index_equal(s.cat.categories, exp_categories)
    s.cat.categories = [1, 2, 3]
    exp_categories = Index([1, 2, 3])
    tm.assert_index_equal(s.cat.categories, exp_categories)
    exp_codes = Series([0, 1, 2, 0], dtype='int8')
    tm.assert_series_equal(s.cat.codes, exp_codes)
    assert s.cat.ordered
    s = s.cat.as_unordered()
    assert not s.cat.ordered
    s.cat.as_ordered(inplace=True)
    assert s.cat.ordered
    s = Series(Categorical(['a', 'b', 'c', 'a'], ordered=True))
    exp_categories = Index(['c', 'b', 'a'])
    exp_values = np.array(['a', 'b', 'c', 'a'], dtype=np.object_)
    s = s.cat.set_categories(['c', 'b', 'a'])
    tm.assert_index_equal(s.cat.categories, exp_categories)
    tm.assert_numpy_array_equal(s.values.__array__(), exp_values)
    tm.assert_numpy_array_equal(s.__array__(), exp_values)
    s = Series(Categorical(['a', 'b', 'b', 'a'], categories=['a', 'b', 'c']))
    exp_categories = Index(['a', 'b'])
    exp_values = np.array(['a', 'b', 'b', 'a'], dtype=np.object_)
    s = s.cat.remove_unused_categories()
    tm.assert_index_equal(s.cat.categories, exp_categories)
    tm.assert_numpy_array_equal(s.values.__array__(), exp_values)
    tm.assert_numpy_array_equal(s.__array__(), exp_values)
    msg = "'Series' object has no attribute 'set_categories'"
    with pytest.raises(AttributeError, match=msg):
        s.set_categories([4, 3, 2, 1])
    s = Series(Categorical(['a', 'b', 'c', 'a'], ordered=True))
    result = s.cat.rename_categories(lambda x: x.upper())
    expected = Series(Categorical(['A', 'B', 'C', 'A'], categories=['A', 'B', 'C'], ordered=True))
    tm.assert_series_equal(result, expected)