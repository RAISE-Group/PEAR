def test_convert_nested(self):
    inner = [Timestamp('2017-01-01'), Timestamp('2017-01-02')]
    data = [inner, inner]
    result = self.dtc.convert(data, None, None)
    expected = [self.dtc.convert(x, None, None) for x in data]
    assert (np.array(result) == expected).all()