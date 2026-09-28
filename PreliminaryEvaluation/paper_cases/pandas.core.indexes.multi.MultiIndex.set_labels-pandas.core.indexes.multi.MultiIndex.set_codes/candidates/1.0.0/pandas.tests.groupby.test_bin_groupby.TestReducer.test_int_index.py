def test_int_index(self):
    arr = np.random.randn(100, 4)
    msg = 'Must pass either dummy and labels, or neither'
    with pytest.raises(ValueError, match=msg):
        libreduction.compute_reduction(arr, np.sum, labels=Index(np.arange(4)))
    with pytest.raises(ValueError, match=msg):
        libreduction.compute_reduction(arr, np.sum, axis=1, labels=Index(np.arange(100)))
    dummy = Series(0.0, index=np.arange(100))
    result = libreduction.compute_reduction(arr, np.sum, dummy=dummy, labels=Index(np.arange(4)))
    expected = arr.sum(0)
    tm.assert_almost_equal(result, expected)
    dummy = Series(0.0, index=np.arange(4))
    result = libreduction.compute_reduction(arr, np.sum, axis=1, dummy=dummy, labels=Index(np.arange(100)))
    expected = arr.sum(1)
    tm.assert_almost_equal(result, expected)
    result = libreduction.compute_reduction(arr, np.sum, axis=1, dummy=dummy, labels=Index(np.arange(100)))
    tm.assert_almost_equal(result, expected)