@pytest.mark.parametrize('func', ['sum', 'prod', 'any', 'all'])
def test_apply_funcs_over_empty(self, func):
    df = DataFrame(columns=['a', 'b', 'c'])
    result = df.apply(getattr(np, func))
    expected = getattr(df, func)()
    tm.assert_series_equal(result, expected)