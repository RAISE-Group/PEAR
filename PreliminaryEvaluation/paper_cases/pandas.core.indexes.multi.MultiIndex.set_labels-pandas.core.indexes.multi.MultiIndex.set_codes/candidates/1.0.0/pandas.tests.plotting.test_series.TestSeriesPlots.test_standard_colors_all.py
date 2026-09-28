@pytest.mark.slow
def test_standard_colors_all(self):
    import matplotlib.colors as colors
    from pandas.plotting._matplotlib.style import _get_standard_colors
    for c in colors.cnames:
        result = _get_standard_colors(num_colors=1, color=c)
        assert result == [c]
        result = _get_standard_colors(num_colors=1, color=[c])
        assert result == [c]
        result = _get_standard_colors(num_colors=3, color=c)
        assert result == [c] * 3
        result = _get_standard_colors(num_colors=3, color=[c])
        assert result == [c] * 3
    for c in colors.ColorConverter.colors:
        result = _get_standard_colors(num_colors=1, color=c)
        assert result == [c]
        result = _get_standard_colors(num_colors=1, color=[c])
        assert result == [c]
        result = _get_standard_colors(num_colors=3, color=c)
        assert result == [c] * 3
        result = _get_standard_colors(num_colors=3, color=[c])
        assert result == [c] * 3