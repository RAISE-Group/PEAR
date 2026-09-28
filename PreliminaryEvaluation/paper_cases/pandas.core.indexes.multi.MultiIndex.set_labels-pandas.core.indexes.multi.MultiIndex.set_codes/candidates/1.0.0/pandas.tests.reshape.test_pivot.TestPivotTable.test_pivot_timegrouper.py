def test_pivot_timegrouper(self):
    df = DataFrame({'Branch': 'A A A A A A A B'.split(), 'Buyer': 'Carl Mark Carl Carl Joe Joe Joe Carl'.split(), 'Quantity': [1, 3, 5, 1, 8, 1, 9, 3], 'Date': [datetime(2013, 1, 1), datetime(2013, 1, 1), datetime(2013, 10, 1), datetime(2013, 10, 2), datetime(2013, 10, 1), datetime(2013, 10, 2), datetime(2013, 12, 2), datetime(2013, 12, 2)]}).set_index('Date')
    expected = DataFrame(np.array([10, 18, 3], dtype='int64').reshape(1, 3), index=[datetime(2013, 12, 31)], columns='Carl Joe Mark'.split())
    expected.index.name = 'Date'
    expected.columns.name = 'Buyer'
    result = pivot_table(df, index=Grouper(freq='A'), columns='Buyer', values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected)
    result = pivot_table(df, index='Buyer', columns=Grouper(freq='A'), values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected.T)
    expected = DataFrame(np.array([1, np.nan, 3, 9, 18, np.nan]).reshape(2, 3), index=[datetime(2013, 1, 1), datetime(2013, 7, 1)], columns='Carl Joe Mark'.split())
    expected.index.name = 'Date'
    expected.columns.name = 'Buyer'
    result = pivot_table(df, index=Grouper(freq='6MS'), columns='Buyer', values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected)
    result = pivot_table(df, index='Buyer', columns=Grouper(freq='6MS'), values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected.T)
    df = df.reset_index()
    result = pivot_table(df, index=Grouper(freq='6MS', key='Date'), columns='Buyer', values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected)
    result = pivot_table(df, index='Buyer', columns=Grouper(freq='6MS', key='Date'), values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected.T)
    msg = "'The grouper name foo is not found'"
    with pytest.raises(KeyError, match=msg):
        pivot_table(df, index=Grouper(freq='6MS', key='foo'), columns='Buyer', values='Quantity', aggfunc=np.sum)
    with pytest.raises(KeyError, match=msg):
        pivot_table(df, index='Buyer', columns=Grouper(freq='6MS', key='foo'), values='Quantity', aggfunc=np.sum)
    df = df.set_index('Date')
    result = pivot_table(df, index=Grouper(freq='6MS', level='Date'), columns='Buyer', values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected)
    result = pivot_table(df, index='Buyer', columns=Grouper(freq='6MS', level='Date'), values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected.T)
    msg = 'The level foo is not valid'
    with pytest.raises(ValueError, match=msg):
        pivot_table(df, index=Grouper(freq='6MS', level='foo'), columns='Buyer', values='Quantity', aggfunc=np.sum)
    with pytest.raises(ValueError, match=msg):
        pivot_table(df, index='Buyer', columns=Grouper(freq='6MS', level='foo'), values='Quantity', aggfunc=np.sum)
    df = DataFrame({'Branch': 'A A A A A A A B'.split(), 'Buyer': 'Carl Mark Carl Carl Joe Joe Joe Carl'.split(), 'Quantity': [1, 3, 5, 1, 8, 1, 9, 3], 'Date': [datetime(2013, 11, 1, 13, 0), datetime(2013, 9, 1, 13, 5), datetime(2013, 10, 1, 20, 0), datetime(2013, 10, 2, 10, 0), datetime(2013, 11, 1, 20, 0), datetime(2013, 10, 2, 10, 0), datetime(2013, 10, 2, 12, 0), datetime(2013, 12, 5, 14, 0)], 'PayDay': [datetime(2013, 10, 4, 0, 0), datetime(2013, 10, 15, 13, 5), datetime(2013, 9, 5, 20, 0), datetime(2013, 11, 2, 10, 0), datetime(2013, 10, 7, 20, 0), datetime(2013, 9, 5, 10, 0), datetime(2013, 12, 30, 12, 0), datetime(2013, 11, 20, 14, 0)]})
    result = pivot_table(df, index=Grouper(freq='M', key='Date'), columns=Grouper(freq='M', key='PayDay'), values='Quantity', aggfunc=np.sum)
    expected = DataFrame(np.array([np.nan, 3, np.nan, np.nan, 6, np.nan, 1, 9, np.nan, 9, np.nan, np.nan, np.nan, np.nan, 3, np.nan]).reshape(4, 4), index=[datetime(2013, 9, 30), datetime(2013, 10, 31), datetime(2013, 11, 30), datetime(2013, 12, 31)], columns=[datetime(2013, 9, 30), datetime(2013, 10, 31), datetime(2013, 11, 30), datetime(2013, 12, 31)])
    expected.index.name = 'Date'
    expected.columns.name = 'PayDay'
    tm.assert_frame_equal(result, expected)
    result = pivot_table(df, index=Grouper(freq='M', key='PayDay'), columns=Grouper(freq='M', key='Date'), values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected.T)
    tuples = [(datetime(2013, 9, 30), datetime(2013, 10, 31)), (datetime(2013, 10, 31), datetime(2013, 9, 30)), (datetime(2013, 10, 31), datetime(2013, 11, 30)), (datetime(2013, 10, 31), datetime(2013, 12, 31)), (datetime(2013, 11, 30), datetime(2013, 10, 31)), (datetime(2013, 12, 31), datetime(2013, 11, 30))]
    idx = MultiIndex.from_tuples(tuples, names=['Date', 'PayDay'])
    expected = DataFrame(np.array([3, np.nan, 6, np.nan, 1, np.nan, 9, np.nan, 9, np.nan, np.nan, 3]).reshape(6, 2), index=idx, columns=['A', 'B'])
    expected.columns.name = 'Branch'
    result = pivot_table(df, index=[Grouper(freq='M', key='Date'), Grouper(freq='M', key='PayDay')], columns=['Branch'], values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected)
    result = pivot_table(df, index=['Branch'], columns=[Grouper(freq='M', key='Date'), Grouper(freq='M', key='PayDay')], values='Quantity', aggfunc=np.sum)
    tm.assert_frame_equal(result, expected.T)