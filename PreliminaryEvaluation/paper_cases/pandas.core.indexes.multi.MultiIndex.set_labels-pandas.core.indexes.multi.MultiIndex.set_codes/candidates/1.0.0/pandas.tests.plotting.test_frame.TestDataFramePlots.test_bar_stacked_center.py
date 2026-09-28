@pytest.mark.slow
def test_bar_stacked_center(self):
    df = DataFrame({'A': [3] * 5, 'B': list(range(5))}, index=range(5))
    self._check_bar_alignment(df, kind='bar', stacked=True)
    self._check_bar_alignment(df, kind='bar', stacked=True, width=0.9)
    self._check_bar_alignment(df, kind='barh', stacked=True)
    self._check_bar_alignment(df, kind='barh', stacked=True, width=0.9)