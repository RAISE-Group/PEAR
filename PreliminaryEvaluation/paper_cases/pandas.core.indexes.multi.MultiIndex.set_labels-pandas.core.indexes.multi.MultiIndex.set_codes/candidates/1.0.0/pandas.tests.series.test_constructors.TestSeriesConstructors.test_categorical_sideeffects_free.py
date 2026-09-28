def test_categorical_sideeffects_free(self):
    cat = Categorical(['a', 'b', 'c', 'a'])
    s = Series(cat, copy=True)
    assert s.cat is not cat
    s.cat.categories = [1, 2, 3]
    exp_s = np.array([1, 2, 3, 1], dtype=np.int64)
    exp_cat = np.array(['a', 'b', 'c', 'a'], dtype=np.object_)
    tm.assert_numpy_array_equal(s.__array__(), exp_s)
    tm.assert_numpy_array_equal(cat.__array__(), exp_cat)
    s[0] = 2
    exp_s2 = np.array([2, 2, 3, 1], dtype=np.int64)
    tm.assert_numpy_array_equal(s.__array__(), exp_s2)
    tm.assert_numpy_array_equal(cat.__array__(), exp_cat)
    cat = Categorical(['a', 'b', 'c', 'a'])
    s = Series(cat)
    assert s.values is cat
    s.cat.categories = [1, 2, 3]
    exp_s = np.array([1, 2, 3, 1], dtype=np.int64)
    tm.assert_numpy_array_equal(s.__array__(), exp_s)
    tm.assert_numpy_array_equal(cat.__array__(), exp_s)
    s[0] = 2
    exp_s2 = np.array([2, 2, 3, 1], dtype=np.int64)
    tm.assert_numpy_array_equal(s.__array__(), exp_s2)
    tm.assert_numpy_array_equal(cat.__array__(), exp_s2)