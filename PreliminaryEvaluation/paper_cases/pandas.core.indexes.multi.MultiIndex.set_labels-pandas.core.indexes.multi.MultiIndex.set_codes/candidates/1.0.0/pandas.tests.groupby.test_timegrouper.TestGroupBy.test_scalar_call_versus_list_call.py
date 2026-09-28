def test_scalar_call_versus_list_call(self):
    data_frame = {'location': ['shanghai', 'beijing', 'shanghai'], 'time': pd.Series(['2017-08-09 13:32:23', '2017-08-11 23:23:15', '2017-08-11 22:23:15'], dtype='datetime64[ns]'), 'value': [1, 2, 3]}
    data_frame = pd.DataFrame(data_frame).set_index('time')
    grouper = pd.Grouper(freq='D')
    grouped = data_frame.groupby(grouper)
    result = grouped.count()
    grouped = data_frame.groupby([grouper])
    expected = grouped.count()
    tm.assert_frame_equal(result, expected)