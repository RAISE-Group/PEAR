def test_get_standard_colors_default_num_colors(self):
    from pandas.plotting._matplotlib.style import _get_standard_colors
    color1 = _get_standard_colors(1, color_type='default')
    color2 = _get_standard_colors(9, color_type='default')
    color3 = _get_standard_colors(20, color_type='default')
    assert len(color1) == 1
    assert len(color2) == 9
    assert len(color3) == 20