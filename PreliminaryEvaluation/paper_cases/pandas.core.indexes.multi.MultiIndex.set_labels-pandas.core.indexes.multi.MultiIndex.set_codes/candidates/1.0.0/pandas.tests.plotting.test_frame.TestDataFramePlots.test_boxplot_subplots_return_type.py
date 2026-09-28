@pytest.mark.slow
def test_boxplot_subplots_return_type(self):
    df = self.hist_df
    result = df.plot.box(subplots=True)
    assert isinstance(result, Series)
    self._check_box_return_type(result, None, expected_keys=['height', 'weight', 'category'])
    for t in ['dict', 'axes', 'both']:
        returned = df.plot.box(return_type=t, subplots=True)
        self._check_box_return_type(returned, t, expected_keys=['height', 'weight', 'category'], check_ax_title=False)