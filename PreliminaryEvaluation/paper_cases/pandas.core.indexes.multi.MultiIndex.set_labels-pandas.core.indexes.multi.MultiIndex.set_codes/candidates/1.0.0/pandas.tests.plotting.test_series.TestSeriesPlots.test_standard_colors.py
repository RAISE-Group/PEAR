@pytest.mark.slow
def test_standard_colors(self):
    from pandas.plotting._matplotlib.style import _get_standard_colors
    for c in ['r', 'red', 'green', '#FF0000']:
        result = _get_standard_colors(1, color=c)
        assert result == [c]
        result = _get_standard_colors(1, color=[c])
        assert result == [c]
        result = _get_standard_colors(3, color=c)
        assert result == [c] * 3
        result = _get_standard_colors(3, color=[c])
        assert result == [c] * 3