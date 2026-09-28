def test_option_no_warning(self):
    pytest.importorskip('matplotlib.pyplot')
    ctx = cf.option_context('plotting.matplotlib.register_converters', False)
    plt = pytest.importorskip('matplotlib.pyplot')
    s = Series(range(12), index=date_range('2017', periods=12))
    _, ax = plt.subplots()
    with ctx:
        with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
            ax.plot(s.index, s.values)
    register_matplotlib_converters()
    with ctx:
        with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
            ax.plot(s.index, s.values)