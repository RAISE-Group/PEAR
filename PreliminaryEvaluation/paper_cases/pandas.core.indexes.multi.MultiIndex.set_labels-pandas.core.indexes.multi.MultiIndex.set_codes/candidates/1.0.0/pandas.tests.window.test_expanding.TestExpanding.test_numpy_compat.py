@pytest.mark.parametrize('method', ['std', 'mean', 'sum', 'max', 'min', 'var'])
def test_numpy_compat(self, method):
    e = Expanding(Series([2, 4, 6]), window=2)
    msg = 'numpy operations are not valid with window objects'
    with pytest.raises(UnsupportedFunctionCall, match=msg):
        getattr(e, method)(1, 2, 3)
    with pytest.raises(UnsupportedFunctionCall, match=msg):
        getattr(e, method)(dtype=np.float64)