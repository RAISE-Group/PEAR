@pytest.mark.slow
def test_boxplot_legacy1(self):
    df = DataFrame(np.random.randn(6, 4), index=list(string.ascii_letters[:6]), columns=['one', 'two', 'three', 'four'])
    df['indic'] = ['foo', 'bar'] * 3
    df['indic2'] = ['foo', 'bar', 'foo'] * 2
    _check_plot_works(df.boxplot, return_type='dict')
    _check_plot_works(df.boxplot, column=['one', 'two'], return_type='dict')
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(df.boxplot, column=['one', 'two'], by='indic')
    _check_plot_works(df.boxplot, column='one', by=['indic', 'indic2'])
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(df.boxplot, by='indic')
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(df.boxplot, by=['indic', 'indic2'])
    _check_plot_works(plotting._core.boxplot, data=df['one'], return_type='dict')
    _check_plot_works(df.boxplot, notch=1, return_type='dict')
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(df.boxplot, by='indic', notch=1)