def test_argsort_stable(self):
    s = Series(np.random.randint(0, 100, size=10000))
    mindexer = s.argsort(kind='mergesort')
    qindexer = s.argsort()
    mexpected = np.argsort(s.values, kind='mergesort')
    qexpected = np.argsort(s.values, kind='quicksort')
    tm.assert_series_equal(mindexer, Series(mexpected), check_dtype=False)
    tm.assert_series_equal(qindexer, Series(qexpected), check_dtype=False)
    msg = "ndarray Expected type <class 'numpy\\.ndarray'>, found <class 'pandas\\.core\\.series\\.Series'> instead"
    with pytest.raises(AssertionError, match=msg):
        tm.assert_numpy_array_equal(qindexer, mindexer)