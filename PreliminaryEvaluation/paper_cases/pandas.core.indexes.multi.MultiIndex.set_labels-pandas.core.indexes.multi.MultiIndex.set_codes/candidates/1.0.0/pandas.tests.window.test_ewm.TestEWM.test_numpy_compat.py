@pytest.mark.parametrize('method', ['std', 'mean', 'var'])
def test_numpy_compat(self, method):
    e = EWM(Series([2, 4, 6]), alpha=0.5)
    msg = 'numpy operations are not valid with window objects'
    with pytest.raises(UnsupportedFunctionCall, match=msg):
        getattr(e, method)(1, 2, 3)
    with pytest.raises(UnsupportedFunctionCall, match=msg):
        getattr(e, method)(dtype=np.float64)