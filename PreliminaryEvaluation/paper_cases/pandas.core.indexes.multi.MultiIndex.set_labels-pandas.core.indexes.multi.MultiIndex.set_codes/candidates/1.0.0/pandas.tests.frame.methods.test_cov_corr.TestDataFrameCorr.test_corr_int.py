def test_corr_int(self):
    df3 = DataFrame({'a': [1, 2, 3, 4], 'b': [1, 2, 3, 4]})
    df3.cov()
    df3.corr()