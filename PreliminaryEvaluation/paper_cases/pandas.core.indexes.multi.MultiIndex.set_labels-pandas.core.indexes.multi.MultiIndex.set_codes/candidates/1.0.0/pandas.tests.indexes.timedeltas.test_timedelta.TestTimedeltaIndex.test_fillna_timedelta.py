def test_fillna_timedelta(self):
    idx = pd.TimedeltaIndex(['1 day', pd.NaT, '3 day'])
    exp = pd.TimedeltaIndex(['1 day', '2 day', '3 day'])
    tm.assert_index_equal(idx.fillna(pd.Timedelta('2 day')), exp)
    exp = pd.TimedeltaIndex(['1 day', '3 hour', '3 day'])
    idx.fillna(pd.Timedelta('3 hour'))
    exp = pd.Index([pd.Timedelta('1 day'), 'x', pd.Timedelta('3 day')], dtype=object)
    tm.assert_index_equal(idx.fillna('x'), exp)