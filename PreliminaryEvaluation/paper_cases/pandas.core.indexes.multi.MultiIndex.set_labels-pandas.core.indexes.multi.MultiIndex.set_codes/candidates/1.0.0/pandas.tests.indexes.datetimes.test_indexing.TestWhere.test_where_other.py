def test_where_other(self):
    i = pd.date_range('20130101', periods=3, tz='US/Eastern')
    for arr in [np.nan, pd.NaT]:
        result = i.where(notna(i), other=np.nan)
        expected = i
        tm.assert_index_equal(result, expected)
    i2 = i.copy()
    i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
    result = i.where(notna(i2), i2)
    tm.assert_index_equal(result, i2)
    i2 = i.copy()
    i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
    result = i.where(notna(i2), i2._values)
    tm.assert_index_equal(result, i2)