@pytest.mark.parametrize('unit', ['ns', 'us', 'ms', 's', 'h', 'm', 'D'])
def test_astype_to_incorrect_datetimelike(self, unit):
    dtype = 'M8[{}]'.format(unit)
    other = 'm8[{}]'.format(unit)
    df = DataFrame(np.array([[1, 2, 3]], dtype=dtype))
    msg = 'cannot astype a datetimelike from \\[datetime64\\[ns\\]\\] to \\[timedelta64\\[{}\\]\\]'.format(unit)
    with pytest.raises(TypeError, match=msg):
        df.astype(other)
    msg = 'cannot astype a timedelta from \\[timedelta64\\[ns\\]\\] to \\[datetime64\\[{}\\]\\]'.format(unit)
    df = DataFrame(np.array([[1, 2, 3]], dtype=other))
    with pytest.raises(TypeError, match=msg):
        df.astype(dtype)