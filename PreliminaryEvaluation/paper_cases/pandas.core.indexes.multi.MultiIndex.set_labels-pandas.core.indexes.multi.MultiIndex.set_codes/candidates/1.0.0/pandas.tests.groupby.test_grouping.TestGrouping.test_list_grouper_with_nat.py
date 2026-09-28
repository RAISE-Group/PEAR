def test_list_grouper_with_nat(self):
    df = pd.DataFrame({'date': pd.date_range('1/1/2011', periods=365, freq='D')})
    df.iloc[-1] = pd.NaT
    grouper = pd.Grouper(key='date', freq='AS')
    result = df.groupby([grouper])
    expected = {pd.Timestamp('2011-01-01'): pd.Index(list(range(364)))}
    tm.assert_dict_equal(result.groups, expected)
    result = df.groupby(grouper)
    expected = {pd.Timestamp('2011-01-01'): 365}
    tm.assert_dict_equal(result.groups, expected)