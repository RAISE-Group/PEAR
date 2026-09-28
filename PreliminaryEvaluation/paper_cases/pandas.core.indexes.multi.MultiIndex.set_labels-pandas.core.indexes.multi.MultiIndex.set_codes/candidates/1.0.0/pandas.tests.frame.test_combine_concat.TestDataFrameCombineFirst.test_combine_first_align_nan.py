def test_combine_first_align_nan(self):
    dfa = pd.DataFrame([[pd.Timestamp('2011-01-01'), 2]], columns=['a', 'b'])
    dfb = pd.DataFrame([[4], [5]], columns=['b'])
    assert dfa['a'].dtype == 'datetime64[ns]'
    assert dfa['b'].dtype == 'int64'
    res = dfa.combine_first(dfb)
    exp = pd.DataFrame({'a': [pd.Timestamp('2011-01-01'), pd.NaT], 'b': [2.0, 5.0]}, columns=['a', 'b'])
    tm.assert_frame_equal(res, exp)
    assert res['a'].dtype == 'datetime64[ns]'
    assert res['b'].dtype == 'float64'
    res = dfa.iloc[:0].combine_first(dfb)
    exp = pd.DataFrame({'a': [np.nan, np.nan], 'b': [4, 5]}, columns=['a', 'b'])
    tm.assert_frame_equal(res, exp)
    assert res['a'].dtype == 'float64'
    assert res['b'].dtype == 'int64'