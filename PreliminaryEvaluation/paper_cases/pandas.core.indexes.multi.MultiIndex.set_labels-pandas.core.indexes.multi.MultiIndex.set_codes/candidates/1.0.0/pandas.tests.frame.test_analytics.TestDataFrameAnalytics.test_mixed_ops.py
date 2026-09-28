@pytest.mark.parametrize('op', ['mean', 'std', 'var', 'skew', 'kurt', 'sem'])
def test_mixed_ops(self, op):
    df = DataFrame({'int': [1, 2, 3, 4], 'float': [1.0, 2.0, 3.0, 4.0], 'str': ['a', 'b', 'c', 'd']})
    result = getattr(df, op)()
    assert len(result) == 2
    with pd.option_context('use_bottleneck', False):
        result = getattr(df, op)()
        assert len(result) == 2