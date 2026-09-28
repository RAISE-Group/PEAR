@pytest.mark.slow
def test_df_grid_settings(self):
    self._check_grid_settings(DataFrame({'a': [1, 2, 3], 'b': [2, 3, 4]}), plotting.PlotAccessor._dataframe_kinds, kws={'x': 'a', 'y': 'b'})