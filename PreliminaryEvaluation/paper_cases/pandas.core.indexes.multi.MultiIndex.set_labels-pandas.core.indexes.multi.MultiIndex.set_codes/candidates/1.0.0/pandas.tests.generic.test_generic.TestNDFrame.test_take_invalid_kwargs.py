def test_take_invalid_kwargs(self):
    indices = [-3, 2, 0, 1]
    s = tm.makeFloatSeries()
    df = tm.makeTimeDataFrame()
    for obj in (s, df):
        msg = "take\\(\\) got an unexpected keyword argument 'foo'"
        with pytest.raises(TypeError, match=msg):
            obj.take(indices, foo=2)
        msg = "the 'out' parameter is not supported"
        with pytest.raises(ValueError, match=msg):
            obj.take(indices, out=indices)
        msg = "the 'mode' parameter is not supported"
        with pytest.raises(ValueError, match=msg):
            obj.take(indices, mode='clip')