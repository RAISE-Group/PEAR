def test_concat_timedelta64_block(self):
    from pandas import to_timedelta
    rng = to_timedelta(np.arange(10), unit='s')
    df = DataFrame({'time': rng})
    result = concat([df, df])
    assert (result.iloc[:10]['time'] == rng).all()
    assert (result.iloc[10:]['time'] == rng).all()