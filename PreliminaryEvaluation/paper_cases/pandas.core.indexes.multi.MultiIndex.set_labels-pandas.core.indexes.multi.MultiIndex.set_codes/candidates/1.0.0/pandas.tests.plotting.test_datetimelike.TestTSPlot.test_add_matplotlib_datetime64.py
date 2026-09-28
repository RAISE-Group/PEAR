@pytest.mark.xfail(reason='GH9053 matplotlib does not use ax.xaxis.converter')
def test_add_matplotlib_datetime64(self):
    s = Series(np.random.randn(10), index=date_range('1970-01-02', periods=10))
    ax = s.plot()
    ax.plot(s.index, s.values, color='g')
    l1, l2 = ax.lines
    tm.assert_numpy_array_equal(l1.get_xydata(), l2.get_xydata())