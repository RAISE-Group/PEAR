def test_grouper_getting_correct_binner(self):
    df = DataFrame({'A': 1}, index=pd.MultiIndex.from_product([list('ab'), date_range('20130101', periods=80)], names=['one', 'two']))
    result = df.groupby([pd.Grouper(level='one'), pd.Grouper(level='two', freq='M')]).sum()
    expected = DataFrame({'A': [31, 28, 21, 31, 28, 21]}, index=MultiIndex.from_product([list('ab'), date_range('20130101', freq='M', periods=3)], names=['one', 'two']))
    tm.assert_frame_equal(result, expected)