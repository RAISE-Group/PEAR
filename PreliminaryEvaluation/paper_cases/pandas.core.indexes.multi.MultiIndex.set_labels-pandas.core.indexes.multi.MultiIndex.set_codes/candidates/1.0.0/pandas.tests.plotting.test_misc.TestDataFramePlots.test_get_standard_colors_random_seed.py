def test_get_standard_colors_random_seed(self):
    df = DataFrame(np.zeros((10, 10)))
    plotting.parallel_coordinates(df, 0)
    rand1 = random.random()
    plotting.parallel_coordinates(df, 0)
    rand2 = random.random()
    assert rand1 != rand2
    from pandas.plotting._matplotlib.style import _get_standard_colors
    color1 = _get_standard_colors(1, color_type='random')
    color2 = _get_standard_colors(1, color_type='random')
    assert color1 == color2