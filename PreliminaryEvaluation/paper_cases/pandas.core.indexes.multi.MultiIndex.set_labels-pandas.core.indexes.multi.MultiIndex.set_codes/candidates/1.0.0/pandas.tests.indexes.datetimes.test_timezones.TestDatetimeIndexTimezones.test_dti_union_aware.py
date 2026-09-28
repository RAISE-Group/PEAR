def test_dti_union_aware(self):
    rng = date_range('2012-11-15 00:00:00', periods=6, freq='H', tz='US/Central')
    rng2 = date_range('2012-11-15 12:00:00', periods=6, freq='H', tz='US/Eastern')
    result = rng.union(rng2)
    expected = rng.astype('O').union(rng2.astype('O'))
    tm.assert_index_equal(result, expected)
    assert result[0].tz.zone == 'US/Central'
    assert result[-1].tz.zone == 'US/Eastern'