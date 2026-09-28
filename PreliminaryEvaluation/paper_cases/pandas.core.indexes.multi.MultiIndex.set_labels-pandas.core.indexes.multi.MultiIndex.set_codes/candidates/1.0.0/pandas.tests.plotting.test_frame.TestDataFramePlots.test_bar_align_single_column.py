@pytest.mark.slow
def test_bar_align_single_column(self):
    df = DataFrame(randn(5))
    self._check_bar_alignment(df, kind='bar', stacked=False)
    self._check_bar_alignment(df, kind='bar', stacked=True)
    self._check_bar_alignment(df, kind='barh', stacked=False)
    self._check_bar_alignment(df, kind='barh', stacked=True)
    self._check_bar_alignment(df, kind='bar', subplots=True)
    self._check_bar_alignment(df, kind='barh', subplots=True)