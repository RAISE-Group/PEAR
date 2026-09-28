@pytest.mark.parametrize('method', ['sum', 'mean'])
def test_numpy_compat(self, method):
    w = Window(Series([2, 4, 6]), window=[0, 2])
    msg = 'numpy operations are not valid with window objects'
    with pytest.raises(UnsupportedFunctionCall, match=msg):
        getattr(w, method)(1, 2, 3)
    with pytest.raises(UnsupportedFunctionCall, match=msg):
        getattr(w, method)(dtype=np.float64)