@pytest.mark.slow
def test_boxplot_return_type(self):
    df = DataFrame(randn(6, 4), index=list(string.ascii_letters[:6]), columns=['one', 'two', 'three', 'four'])
    with pytest.raises(ValueError):
        df.plot.box(return_type='NOTATYPE')
    result = df.plot.box(return_type='dict')
    self._check_box_return_type(result, 'dict')
    result = df.plot.box(return_type='axes')
    self._check_box_return_type(result, 'axes')
    result = df.plot.box()
    self._check_box_return_type(result, 'axes')
    result = df.plot.box(return_type='both')
    self._check_box_return_type(result, 'both')