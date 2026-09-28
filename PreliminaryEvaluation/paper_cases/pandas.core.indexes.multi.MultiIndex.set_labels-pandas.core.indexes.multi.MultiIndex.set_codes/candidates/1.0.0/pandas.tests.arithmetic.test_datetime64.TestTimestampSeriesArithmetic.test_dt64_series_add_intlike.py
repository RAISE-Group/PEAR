@pytest.mark.parametrize('op', ['__add__', '__radd__', '__sub__', '__rsub__'])
@pytest.mark.parametrize('tz', [None, 'Asia/Tokyo'])
def test_dt64_series_add_intlike(self, tz, op):
    dti = pd.DatetimeIndex(['2016-01-02', '2016-02-03', 'NaT'], tz=tz)
    ser = Series(dti)
    other = Series([20, 30, 40], dtype='uint8')
    method = getattr(ser, op)
    msg = '|'.join(['Addition/subtraction of integers and integer-arrays', 'cannot subtract .* from ndarray'])
    with pytest.raises(TypeError, match=msg):
        method(1)
    with pytest.raises(TypeError, match=msg):
        method(other)
    with pytest.raises(TypeError, match=msg):
        method(np.array(other))
    with pytest.raises(TypeError, match=msg):
        method(pd.Index(other))