@pytest.mark.parametrize('floats', [[1.1, 2.1], np.array([1.1, 2.1])])
def test_constructor_floats(self, floats):
    msg = 'PeriodIndex\\._simple_new does not accept floats'
    with pytest.raises(TypeError, match=msg):
        pd.PeriodIndex._simple_new(floats, freq='M')
    msg = 'PeriodIndex does not allow floating point in construction'
    with pytest.raises(TypeError, match=msg):
        pd.PeriodIndex(floats, freq='M')