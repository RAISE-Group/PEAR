@pytest.mark.slow
def test_bar_barwidth_position(self):
    df = DataFrame(randn(5, 5))
    self._check_bar_alignment(df, kind='bar', stacked=False, width=0.9, position=0.2)
    self._check_bar_alignment(df, kind='bar', stacked=True, width=0.9, position=0.2)
    self._check_bar_alignment(df, kind='barh', stacked=False, width=0.9, position=0.2)
    self._check_bar_alignment(df, kind='barh', stacked=True, width=0.9, position=0.2)
    self._check_bar_alignment(df, kind='bar', subplots=True, width=0.9, position=0.2)
    self._check_bar_alignment(df, kind='barh', subplots=True, width=0.9, position=0.2)