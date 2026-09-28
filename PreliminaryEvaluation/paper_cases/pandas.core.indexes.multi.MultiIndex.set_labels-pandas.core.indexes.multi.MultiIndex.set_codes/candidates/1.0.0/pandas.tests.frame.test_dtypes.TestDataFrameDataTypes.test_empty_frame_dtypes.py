def test_empty_frame_dtypes(self):
    empty_df = pd.DataFrame()
    tm.assert_series_equal(empty_df.dtypes, pd.Series(dtype=np.object))
    nocols_df = pd.DataFrame(index=[1, 2, 3])
    tm.assert_series_equal(nocols_df.dtypes, pd.Series(dtype=np.object))
    norows_df = pd.DataFrame(columns=list('abc'))
    tm.assert_series_equal(norows_df.dtypes, pd.Series(np.object, index=list('abc')))
    norows_int_df = pd.DataFrame(columns=list('abc')).astype(np.int32)
    tm.assert_series_equal(norows_int_df.dtypes, pd.Series(np.dtype('int32'), index=list('abc')))
    odict = OrderedDict
    df = pd.DataFrame(odict([('a', 1), ('b', True), ('c', 1.0)]), index=[1, 2, 3])
    ex_dtypes = pd.Series(odict([('a', np.int64), ('b', np.bool), ('c', np.float64)]))
    tm.assert_series_equal(df.dtypes, ex_dtypes)
    tm.assert_series_equal(df[:0].dtypes, ex_dtypes)