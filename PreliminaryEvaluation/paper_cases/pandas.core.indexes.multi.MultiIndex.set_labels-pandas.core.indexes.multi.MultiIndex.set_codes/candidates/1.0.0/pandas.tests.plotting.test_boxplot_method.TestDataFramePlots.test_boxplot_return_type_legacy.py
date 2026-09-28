@pytest.mark.slow
def test_boxplot_return_type_legacy(self):
    import matplotlib as mpl
    df = DataFrame(np.random.randn(6, 4), index=list(string.ascii_letters[:6]), columns=['one', 'two', 'three', 'four'])
    with pytest.raises(ValueError):
        df.boxplot(return_type='NOTATYPE')
    result = df.boxplot()
    self._check_box_return_type(result, 'axes')
    with tm.assert_produces_warning(False):
        result = df.boxplot(return_type='dict')
    self._check_box_return_type(result, 'dict')
    with tm.assert_produces_warning(False):
        result = df.boxplot(return_type='axes')
    self._check_box_return_type(result, 'axes')
    with tm.assert_produces_warning(False):
        result = df.boxplot(return_type='both')
    self._check_box_return_type(result, 'both')