def test_repr_non_interactive(self):
    df = DataFrame('hello', index=range(1000), columns=range(5))
    with option_context('mode.sim_interactive', False, 'display.width', 0, 'display.max_rows', 5000):
        assert not has_truncated_repr(df)
        assert not has_expanded_repr(df)