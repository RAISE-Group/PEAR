@pytest.mark.parametrize('func,expected', [('transform', pd.Series(name=2, dtype=np.float64, index=pd.RangeIndex(0, 0, 1))), ('agg', pd.Series(name=2, dtype=np.float64, index=pd.Float64Index([], name=1))), ('apply', pd.Series(name=2, dtype=np.float64, index=pd.Float64Index([], name=1)))])
def test_evaluate_with_empty_groups(self, func, expected):
    df = pd.DataFrame({1: [], 2: []})
    g = df.groupby(1)
    result = getattr(g[2], func)(lambda x: x)
    tm.assert_series_equal(result, expected)