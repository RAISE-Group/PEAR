def test_bar_user_colors(self):
    df = pd.DataFrame({'A': range(4), 'B': range(1, 5), 'color': ['red', 'blue', 'blue', 'red']})
    ax = df.plot.bar(y='A', color=df['color'])
    result = [p.get_facecolor() for p in ax.patches]
    expected = [(1.0, 0.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0), (0.0, 0.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0)]
    assert result == expected