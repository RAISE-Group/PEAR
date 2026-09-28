def test_take_bad_bounds_raises(self):
    index = pd.Index(list('ABC'), name='xxx')
    with pytest.raises(IndexError, match='out of bounds'):
        index.take(np.array([1, -5]))