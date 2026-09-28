def test_style_single_ok(self):
    s = pd.Series([1, 2])
    ax = s.plot(style='s', color='C3')
    assert ax.lines[0].get_color() == ['C3']