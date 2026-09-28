def test_wide_repr_wide_long_columns(self):
    with option_context('mode.sim_interactive', True):
        df = DataFrame({'a': ['a' * 30, 'b' * 30], 'b': ['c' * 70, 'd' * 80]})
        result = repr(df)
        assert 'ccccc' in result
        assert 'ddddd' in result