def test_color_and_style_arguments(self):
    df = DataFrame({'x': [1, 2], 'y': [3, 4]})
    ax = df.plot(color=['red', 'black'], style=['-', '--'])
    linestyle = [line.get_linestyle() for line in ax.lines]
    assert linestyle == ['-', '--']
    color = [line.get_color() for line in ax.lines]
    assert color == ['red', 'black']
    with pytest.raises(ValueError):
        df.plot(color=['red', 'black'], style=['k-', 'r--'])