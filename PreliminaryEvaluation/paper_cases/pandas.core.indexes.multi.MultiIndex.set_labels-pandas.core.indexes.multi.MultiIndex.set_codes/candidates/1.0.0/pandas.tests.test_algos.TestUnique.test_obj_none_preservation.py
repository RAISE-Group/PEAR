def test_obj_none_preservation(self):
    arr = np.array(['foo', None], dtype=object)
    result = pd.unique(arr)
    expected = np.array(['foo', None], dtype=object)
    tm.assert_numpy_array_equal(result, expected, strict_nan=True)