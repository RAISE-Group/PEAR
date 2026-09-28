@pytest.mark.parametrize('df', [pd.DataFrame({'A': ['a', None], 'B': ['c', 'd']})])
@pytest.mark.parametrize('method', ['min', 'max', 'sum'])
def test_consistency_of_aggregates_of_columns_with_missing_values(self, df, method):
    none_in_first_column_result = getattr(df[['A', 'B']], method)()
    none_in_second_column_result = getattr(df[['B', 'A']], method)()
    tm.assert_series_equal(none_in_first_column_result, none_in_second_column_result)