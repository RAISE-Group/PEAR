def test_setitem_datetime_coercion(self):
    df = pd.DataFrame({'c': [pd.Timestamp('2010-10-01')] * 3})
    df.loc[0:1, 'c'] = np.datetime64('2008-08-08')
    assert pd.Timestamp('2008-08-08') == df.loc[0, 'c']
    assert pd.Timestamp('2008-08-08') == df.loc[1, 'c']
    df.loc[2, 'c'] = date(2005, 5, 5)
    assert pd.Timestamp('2005-05-05') == df.loc[2, 'c']