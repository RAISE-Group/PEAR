@td.skip_if_no_scipy
@pytest.mark.parametrize('method', ['polynomial', 'spline'])
def test_no_order(self, method):
    s = Series([0, 1, np.nan, 3])
    msg = 'You must specify the order of the spline or polynomial'
    with pytest.raises(ValueError, match=msg):
        s.interpolate(method=method)