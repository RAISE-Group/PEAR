def test_matplotlib_formatters(self):
    units = pytest.importorskip('matplotlib.units')
    with cf.option_context('plotting.matplotlib.register_converters', True):
        with cf.option_context('plotting.matplotlib.register_converters', False):
            assert Timestamp not in units.registry
        assert Timestamp in units.registry