def test_concat_datetime64_block(self):
    from pandas.core.indexes.datetimes import date_range
    rng = date_range('1/1/2000', periods=10)
    df = DataFrame({'time': rng})
    result = concat([df, df])
    assert (result.iloc[:10]['time'] == rng).all()
    assert (result.iloc[10:]['time'] == rng).all()