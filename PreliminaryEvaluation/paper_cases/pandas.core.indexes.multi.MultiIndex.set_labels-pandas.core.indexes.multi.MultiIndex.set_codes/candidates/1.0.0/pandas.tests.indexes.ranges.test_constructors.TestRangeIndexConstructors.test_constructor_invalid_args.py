def test_constructor_invalid_args(self):
    msg = 'RangeIndex\\(\\.\\.\\.\\) must be called with integers'
    with pytest.raises(TypeError, match=msg):
        RangeIndex()
    with pytest.raises(TypeError, match=msg):
        RangeIndex(name='Foo')
    for i in [Index(['a', 'b']), Series(['a', 'b']), np.array(['a', 'b']), [], 'foo', datetime(2000, 1, 1, 0, 0), np.arange(0, 10), np.array([1]), [1]]:
        with pytest.raises(TypeError):
            RangeIndex(i)
    msg = 'Index\\(\\.\\.\\.\\) must be called with a collection of some kind, 0 was passed'
    with pytest.raises(TypeError, match=msg):
        Index(0, 1000)