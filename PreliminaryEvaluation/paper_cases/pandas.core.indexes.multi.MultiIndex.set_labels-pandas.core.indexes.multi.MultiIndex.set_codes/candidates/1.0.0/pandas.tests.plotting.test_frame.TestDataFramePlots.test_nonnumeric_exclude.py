def test_nonnumeric_exclude(self):
    df = DataFrame({'A': ['x', 'y', 'z'], 'B': [1, 2, 3]})
    ax = df.plot()
    assert len(ax.get_lines()) == 1