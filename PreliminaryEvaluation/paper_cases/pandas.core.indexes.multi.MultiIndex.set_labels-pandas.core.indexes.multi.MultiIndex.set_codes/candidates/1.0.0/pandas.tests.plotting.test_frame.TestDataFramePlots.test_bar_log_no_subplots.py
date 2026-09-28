@pytest.mark.slow
def test_bar_log_no_subplots(self):
    expected = np.array([0.1, 1.0, 10.0, 100])
    df = DataFrame({'A': [3] * 5, 'B': list(range(1, 6))}, index=range(5))
    ax = df.plot.bar(grid=True, log=True)
    tm.assert_numpy_array_equal(ax.yaxis.get_ticklocs(), expected)