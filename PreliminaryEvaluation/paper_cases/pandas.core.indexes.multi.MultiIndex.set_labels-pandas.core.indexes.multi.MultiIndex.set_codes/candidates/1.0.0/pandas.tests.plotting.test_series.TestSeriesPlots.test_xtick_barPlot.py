def test_xtick_barPlot(self):
    s = pd.Series(range(10), index=[f'P{i:02d}' for i in range(10)])
    ax = s.plot.bar(xticks=range(0, 11, 2))
    exp = np.array(list(range(0, 11, 2)))
    tm.assert_numpy_array_equal(exp, ax.get_xticks())