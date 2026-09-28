def test_dtypes_are_correct_after_column_slice(self):
    df = pd.DataFrame(index=range(5), columns=list('abc'), dtype=np.float_)
    odict = OrderedDict
    tm.assert_series_equal(df.dtypes, pd.Series(odict([('a', np.float_), ('b', np.float_), ('c', np.float_)])))
    tm.assert_series_equal(df.iloc[:, 2:].dtypes, pd.Series(odict([('c', np.float_)])))
    tm.assert_series_equal(df.dtypes, pd.Series(odict([('a', np.float_), ('b', np.float_), ('c', np.float_)])))