def test_argmin_argmax(self):
    idx = DatetimeIndex(['2000-01-04', '2000-01-01', '2000-01-02'])
    assert idx.argmin() == 1
    assert idx.argmax() == 0