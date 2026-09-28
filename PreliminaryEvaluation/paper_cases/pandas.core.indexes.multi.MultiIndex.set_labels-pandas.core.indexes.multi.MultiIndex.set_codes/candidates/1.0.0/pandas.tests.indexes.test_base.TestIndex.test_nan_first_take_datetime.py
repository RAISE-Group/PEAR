def test_nan_first_take_datetime(self):
    index = Index([pd.NaT, Timestamp('20130101'), Timestamp('20130102')])
    result = index.take([-1, 0, 1])
    expected = Index([index[-1], index[0], index[1]])
    tm.assert_index_equal(result, expected)