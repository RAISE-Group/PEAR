@td.skip_if_no_scipy
@pytest.mark.parametrize('which', ['series', 'frame'])
def test_constructor_with_win_type(self, which, win_types):
    o = getattr(self, which)
    c = o.rolling
    c(win_type=win_types, window=2)