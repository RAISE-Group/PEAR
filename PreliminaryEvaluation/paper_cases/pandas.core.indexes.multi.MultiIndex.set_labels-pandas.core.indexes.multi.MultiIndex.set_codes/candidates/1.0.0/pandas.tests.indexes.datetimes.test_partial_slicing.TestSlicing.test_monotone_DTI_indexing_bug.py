def test_monotone_DTI_indexing_bug(self):
    df = pd.DataFrame(list(range(5)))
    date_list = ['2018-01-02', '2017-02-10', '2016-03-10', '2015-03-15', '2014-03-16']
    date_index = pd.to_datetime(date_list)
    df['date'] = date_index
    expected = pd.DataFrame({0: list(range(5)), 'date': date_index})
    tm.assert_frame_equal(df, expected)
    df = pd.DataFrame({'A': [1, 2, 3]}, index=pd.date_range('20170101', periods=3)[::-1])
    expected = pd.DataFrame({'A': 1}, index=pd.date_range('20170103', periods=1))
    tm.assert_frame_equal(df.loc['2017-01-03'], expected)