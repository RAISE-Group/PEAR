@td.skip_if_no_scipy
@pytest.mark.parametrize('which', ['series', 'frame'])
def test_constructor_with_win_type(self, which):
    o = getattr(self, which)
    c = o.rolling
    with pytest.raises(ValueError):
        c(-1, win_type='boxcar')