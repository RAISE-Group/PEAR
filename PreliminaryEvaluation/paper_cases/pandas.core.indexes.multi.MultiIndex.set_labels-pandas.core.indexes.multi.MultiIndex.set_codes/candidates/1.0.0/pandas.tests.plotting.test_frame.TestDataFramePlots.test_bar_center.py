@pytest.mark.slow
def test_bar_center(self):
    df = DataFrame({'A': [3] * 5, 'B': list(range(5))}, index=range(5))
    self._check_bar_alignment(df, kind='bar', stacked=False)
    self._check_bar_alignment(df, kind='bar', stacked=False, width=0.9)
    self._check_bar_alignment(df, kind='barh', stacked=False)
    self._check_bar_alignment(df, kind='barh', stacked=False, width=0.9)