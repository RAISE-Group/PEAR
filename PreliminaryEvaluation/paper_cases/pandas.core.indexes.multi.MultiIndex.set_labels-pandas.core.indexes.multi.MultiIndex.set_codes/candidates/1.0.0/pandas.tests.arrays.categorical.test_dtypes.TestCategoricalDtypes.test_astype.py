@pytest.mark.parametrize('ordered', [True, False])
def test_astype(self, ordered):
    cat = Categorical(list('abbaaccc'), ordered=ordered)
    result = cat.astype(object)
    expected = np.array(cat)
    tm.assert_numpy_array_equal(result, expected)
    msg = 'could not convert string to float'
    with pytest.raises(ValueError, match=msg):
        cat.astype(float)
    cat = Categorical([0, 1, 2, 2, 1, 0, 1, 0, 2], ordered=ordered)
    result = cat.astype(object)
    expected = np.array(cat, dtype=object)
    tm.assert_numpy_array_equal(result, expected)
    result = cat.astype(int)
    expected = np.array(cat, dtype=np.int)
    tm.assert_numpy_array_equal(result, expected)
    result = cat.astype(float)
    expected = np.array(cat, dtype=np.float)
    tm.assert_numpy_array_equal(result, expected)