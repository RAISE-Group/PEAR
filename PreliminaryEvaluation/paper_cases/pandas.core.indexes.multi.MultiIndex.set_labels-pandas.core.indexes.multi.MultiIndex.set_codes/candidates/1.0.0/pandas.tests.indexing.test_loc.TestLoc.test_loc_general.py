def test_loc_general(self):
    df = DataFrame(np.random.rand(4, 4), columns=['A', 'B', 'C', 'D'], index=['A', 'B', 'C', 'D'])
    result = df.loc[:, 'A':'B'].iloc[0:2, :]
    assert (result.columns == ['A', 'B']).all()
    assert (result.index == ['A', 'B']).all()
    result = DataFrame({'a': [Timestamp('20130101')], 'b': [1]}).iloc[0]
    expected = Series([Timestamp('20130101'), 1], index=['a', 'b'], name=0)
    tm.assert_series_equal(result, expected)
    assert result.dtype == object