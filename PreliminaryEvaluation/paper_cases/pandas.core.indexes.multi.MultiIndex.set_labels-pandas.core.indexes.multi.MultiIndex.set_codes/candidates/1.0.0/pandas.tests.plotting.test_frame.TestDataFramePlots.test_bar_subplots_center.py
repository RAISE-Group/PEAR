@pytest.mark.slow
def test_bar_subplots_center(self):
    df = DataFrame({'A': [3] * 5, 'B': list(range(5))}, index=range(5))
    self._check_bar_alignment(df, kind='bar', subplots=True)
    self._check_bar_alignment(df, kind='bar', subplots=True, width=0.9)
    self._check_bar_alignment(df, kind='barh', subplots=True)
    self._check_bar_alignment(df, kind='barh', subplots=True, width=0.9)