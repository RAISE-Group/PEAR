def test_groupby_grouper_f_sanity_checked(self):
    dates = date_range('01-Jan-2013', periods=12, freq='MS')
    ts = Series(np.random.randn(12), index=dates)
    msg = 'Grouper result violates len\\(labels\\) == len\\(data\\)'
    with pytest.raises(AssertionError, match=msg):
        ts.groupby(lambda key: key[0:6])