@pytest.mark.parametrize('opname', ['eq', 'ne', 'gt', 'lt', 'ge', 'le'])
def test_df_flex_cmp_constant_return_types_empty(self, opname):
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [1.0, 2.0, 3.0]})
    const = 2
    empty = df.iloc[:0]
    result = getattr(empty, opname)(const).dtypes.value_counts()
    tm.assert_series_equal(result, pd.Series([2], index=[np.dtype(bool)]))