def test_grouper_multilevel_freq(self):
    from datetime import date, timedelta
    d0 = date.today() - timedelta(days=14)
    dates = date_range(d0, date.today())
    date_index = pd.MultiIndex.from_product([dates, dates], names=['foo', 'bar'])
    df = pd.DataFrame(np.random.randint(0, 100, 225), index=date_index)
    expected = df.reset_index().groupby([pd.Grouper(key='foo', freq='W'), pd.Grouper(key='bar', freq='W')]).sum()
    expected.columns = pd.Index([0], dtype='int64')
    result = df.groupby([pd.Grouper(level='foo', freq='W'), pd.Grouper(level='bar', freq='W')]).sum()
    tm.assert_frame_equal(result, expected)
    result = df.groupby([pd.Grouper(level=0, freq='W'), pd.Grouper(level=1, freq='W')]).sum()
    tm.assert_frame_equal(result, expected)