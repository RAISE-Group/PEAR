def test_where_tz(self):
    i = pd.date_range('20130101', periods=3, tz='US/Eastern')
    result = i.where(notna(i))
    expected = i
    tm.assert_index_equal(result, expected)
    i2 = i.copy()
    i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
    result = i.where(notna(i2))
    expected = i2
    tm.assert_index_equal(result, expected)