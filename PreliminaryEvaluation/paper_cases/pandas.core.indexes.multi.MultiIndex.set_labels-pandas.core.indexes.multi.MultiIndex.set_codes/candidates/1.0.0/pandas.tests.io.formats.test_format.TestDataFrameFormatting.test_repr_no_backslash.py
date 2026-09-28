def test_repr_no_backslash(self):
    with option_context('mode.sim_interactive', True):
        df = DataFrame(np.random.randn(10, 4))
        assert '\\' not in repr(df)