def test_registering_no_warning(self):
    plt = pytest.importorskip('matplotlib.pyplot')
    s = Series(range(12), index=date_range('2017', periods=12))
    _, ax = plt.subplots()
    register_matplotlib_converters()
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        ax.plot(s.index, s.values)