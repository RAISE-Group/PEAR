def test_take_invalid_kwargs(self):
    idx = timedelta_range('1 day', '31 day', freq='D', name='idx')
    indices = [1, 6, 5, 9, 10, 13, 15, 3]
    msg = "take\\(\\) got an unexpected keyword argument 'foo'"
    with pytest.raises(TypeError, match=msg):
        idx.take(indices, foo=2)
    msg = "the 'out' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        idx.take(indices, out=indices)
    msg = "the 'mode' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        idx.take(indices, mode='clip')