def test_str_bool_return(self):
    index = Index(['a1', 'a2', 'b1', 'b2'])
    result = index.str.startswith('a')
    expected = np.array([True, True, False, False])
    tm.assert_numpy_array_equal(result, expected)
    assert isinstance(result, np.ndarray)