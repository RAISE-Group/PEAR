@td.skip_if_no_scipy
def test_corr_int_and_boolean(self):
    df = DataFrame({'a': [True, False], 'b': [1, 0]})
    expected = DataFrame(np.ones((2, 2)), index=['a', 'b'], columns=['a', 'b'])
    for meth in ['pearson', 'kendall', 'spearman']:
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('ignore', RuntimeWarning)
            result = df.corr(meth)
        tm.assert_frame_equal(result, expected)