def test_nonnumeric_exclude(self):
    idx = date_range('1/1/1987', freq='A', periods=3)
    df = DataFrame({'A': ['x', 'y', 'z'], 'B': [1, 2, 3]}, idx)
    fig, ax = self.plt.subplots()
    df.plot(ax=ax)
    assert len(ax.get_lines()) == 1
    self.plt.close(fig)
    msg = 'no numeric data to plot'
    with pytest.raises(TypeError, match=msg):
        df['A'].plot()