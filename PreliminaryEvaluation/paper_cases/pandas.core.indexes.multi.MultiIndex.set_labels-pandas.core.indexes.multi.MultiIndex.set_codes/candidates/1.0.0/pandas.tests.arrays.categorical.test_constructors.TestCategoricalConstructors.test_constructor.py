def test_constructor(self):
    exp_arr = np.array(['a', 'b', 'c', 'a', 'b', 'c'], dtype=np.object_)
    c1 = Categorical(exp_arr)
    tm.assert_numpy_array_equal(c1.__array__(), exp_arr)
    c2 = Categorical(exp_arr, categories=['a', 'b', 'c'])
    tm.assert_numpy_array_equal(c2.__array__(), exp_arr)
    c2 = Categorical(exp_arr, categories=['c', 'b', 'a'])
    tm.assert_numpy_array_equal(c2.__array__(), exp_arr)
    msg = 'Categorical categories must be unique'
    with pytest.raises(ValueError, match=msg):
        Categorical([1, 2], [1, 2, 2])
    with pytest.raises(ValueError, match=msg):
        Categorical(['a', 'b'], ['a', 'b', 'b'])
    c1 = Categorical(['a', 'b', 'c', 'a'])
    assert not c1.ordered
    c1 = Categorical(['a', 'b', 'c', 'a'])
    c2 = Categorical(c1)
    tm.assert_categorical_equal(c1, c2)
    c1 = Categorical(['a', 'b', 'c', 'a'], categories=['a', 'b', 'c', 'd'])
    c2 = Categorical(c1)
    tm.assert_categorical_equal(c1, c2)
    c1 = Categorical(['a', 'b', 'c', 'a'], categories=['a', 'c', 'b'])
    c2 = Categorical(c1)
    tm.assert_categorical_equal(c1, c2)
    c1 = Categorical(['a', 'b', 'c', 'a'], categories=['a', 'c', 'b'])
    c2 = Categorical(c1, categories=['a', 'b', 'c'])
    tm.assert_numpy_array_equal(c1.__array__(), c2.__array__())
    tm.assert_index_equal(c2.categories, Index(['a', 'b', 'c']))
    c1 = Categorical(['a', 'b', 'c', 'a'], categories=['a', 'b', 'c', 'd'])
    c2 = Categorical(Series(c1))
    tm.assert_categorical_equal(c1, c2)
    c1 = Categorical(['a', 'b', 'c', 'a'], categories=['a', 'c', 'b'])
    c2 = Categorical(Series(c1))
    tm.assert_categorical_equal(c1, c2)
    c1 = Categorical(['a', 'b', 'c', 'a'])
    c2 = Categorical(Series(['a', 'b', 'c', 'a']))
    tm.assert_categorical_equal(c1, c2)
    c1 = Categorical(['a', 'b', 'c', 'a'], categories=['a', 'b', 'c', 'd'])
    c2 = Categorical(Series(['a', 'b', 'c', 'a']), categories=['a', 'b', 'c', 'd'])
    tm.assert_categorical_equal(c1, c2)
    cat = Categorical([1, 2, 3, np.nan], categories=[1, 2, 3])
    assert is_integer_dtype(cat.categories)
    cat = Categorical([np.nan, 1, 2, 3])
    assert is_integer_dtype(cat.categories)
    cat = Categorical([np.nan, 1, 2.0, 3])
    assert is_float_dtype(cat.categories)
    cat = Categorical([np.nan, 1.0, 2.0, 3.0])
    assert is_float_dtype(cat.categories)
    cat = Categorical([1])
    assert len(cat.categories) == 1
    assert cat.categories[0] == 1
    assert len(cat.codes) == 1
    assert cat.codes[0] == 0
    cat = Categorical(['a'])
    assert len(cat.categories) == 1
    assert cat.categories[0] == 'a'
    assert len(cat.codes) == 1
    assert cat.codes[0] == 0
    cat = Categorical(1)
    assert len(cat.categories) == 1
    assert cat.categories[0] == 1
    assert len(cat.codes) == 1
    assert cat.codes[0] == 0
    with tm.assert_produces_warning(None):
        c_old = Categorical([0, 1, 2, 0, 1, 2], categories=['a', 'b', 'c'])
    with tm.assert_produces_warning(None):
        c_old = Categorical([0, 1, 2, 0, 1, 2], categories=[3, 4, 5])
    with tm.assert_produces_warning(None):
        c_old2 = Categorical([0, 1, 2, 0, 1, 2], [1, 2, 3])
        cat = Categorical([1, 2], categories=[1, 2, 3])
    with tm.assert_produces_warning(None):
        c = Categorical(np.array([], dtype='int64'), categories=[3, 2, 1], ordered=True)