def test_constructor_invalid(self):
    msg = 'Float64Index\\(\\.\\.\\.\\) must be called with a collection of some kind, 0\\.0 was passed'
    with pytest.raises(TypeError, match=msg):
        Float64Index(0.0)
    msg = 'String dtype not supported, you may need to explicitly cast to a numeric type'
    with pytest.raises(TypeError, match=msg):
        Float64Index(['a', 'b', 0.0])
    msg = "float\\(\\) argument must be a string or a number, not 'Timestamp'"
    with pytest.raises(TypeError, match=msg):
        Float64Index([Timestamp('20130101')])