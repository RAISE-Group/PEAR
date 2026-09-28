@pytest.mark.skipif(LooseVersion(tables.__version__) < LooseVersion('3.1.0'), reason='tables version does not support fix for nan selection bug: GH 4858')
def test_nan_selection_bug_4858(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = DataFrame(dict(cols=range(6), values=range(6)), dtype='float64')
        df['cols'] = (df['cols'] + 10).apply(str)
        df.iloc[0] = np.nan
        expected = DataFrame(dict(cols=['13.0', '14.0', '15.0'], values=[3.0, 4.0, 5.0]), index=[3, 4, 5])
        store.append('df', df, data_columns=True, index=['cols'])
        result = store.select('df', where='values>2.0')
        tm.assert_frame_equal(result, expected)