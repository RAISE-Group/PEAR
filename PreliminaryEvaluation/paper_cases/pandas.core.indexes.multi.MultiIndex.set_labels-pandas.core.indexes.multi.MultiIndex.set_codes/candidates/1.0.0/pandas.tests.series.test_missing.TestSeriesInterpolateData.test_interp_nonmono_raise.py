@td.skip_if_no_scipy
def test_interp_nonmono_raise(self):
    s = Series([1, np.nan, 3], index=[0, 2, 1])
    msg = 'krogh interpolation requires that the index be monotonic'
    with pytest.raises(ValueError, match=msg):
        s.interpolate(method='krogh')