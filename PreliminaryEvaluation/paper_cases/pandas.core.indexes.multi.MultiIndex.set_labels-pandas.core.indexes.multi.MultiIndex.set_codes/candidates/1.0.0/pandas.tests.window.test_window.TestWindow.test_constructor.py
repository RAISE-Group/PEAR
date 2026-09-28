@td.skip_if_no_scipy
@pytest.mark.parametrize('which', ['series', 'frame'])
def test_constructor(self, which):
    o = getattr(self, which)
    c = o.rolling
    c(win_type='boxcar', window=2, min_periods=1)
    c(win_type='boxcar', window=2, min_periods=1, center=True)
    c(win_type='boxcar', window=2, min_periods=1, center=False)
    for w in [2.0, 'foo', np.array([2])]:
        with pytest.raises(ValueError):
            c(win_type='boxcar', window=2, min_periods=w)
        with pytest.raises(ValueError):
            c(win_type='boxcar', window=2, min_periods=1, center=w)
    for wt in ['foobar', 1]:
        with pytest.raises(ValueError):
            c(win_type=wt, window=2)