def test_append(self):
    rng = date_range('5/8/2012 1:45', periods=10, freq='5T')
    ts = Series(np.random.randn(len(rng)), rng)
    df = DataFrame(np.random.randn(len(rng), 4), index=rng)
    result = ts.append(ts)
    result_df = df.append(df)
    ex_index = DatetimeIndex(np.tile(rng.values, 2))
    tm.assert_index_equal(result.index, ex_index)
    tm.assert_index_equal(result_df.index, ex_index)
    appended = rng.append(rng)
    tm.assert_index_equal(appended, ex_index)
    appended = rng.append([rng, rng])
    ex_index = DatetimeIndex(np.tile(rng.values, 3))
    tm.assert_index_equal(appended, ex_index)
    rng1 = rng.copy()
    rng2 = rng.copy()
    rng1.name = 'foo'
    rng2.name = 'bar'
    assert rng1.append(rng1).name == 'foo'
    assert rng1.append(rng2).name is None