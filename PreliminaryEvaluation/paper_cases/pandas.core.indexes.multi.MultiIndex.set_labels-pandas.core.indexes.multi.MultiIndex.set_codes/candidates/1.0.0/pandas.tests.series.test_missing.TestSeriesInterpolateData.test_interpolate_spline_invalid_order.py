@td.skip_if_no_scipy
@pytest.mark.parametrize('order', [-1, -1.0, 0, 0.0, np.nan])
def test_interpolate_spline_invalid_order(self, order):
    s = Series([0, 1, np.nan, 3])
    msg = 'order needs to be specified and greater than 0'
    with pytest.raises(ValueError, match=msg):
        s.interpolate(method='spline', order=order)