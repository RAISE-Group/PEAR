def test_flex_binary_moment(self):
    msg = 'arguments to moment function must be of type np.ndarray/Series/DataFrame'
    with pytest.raises(TypeError, match=msg):
        _flex_binary_moment(5, 6, None)