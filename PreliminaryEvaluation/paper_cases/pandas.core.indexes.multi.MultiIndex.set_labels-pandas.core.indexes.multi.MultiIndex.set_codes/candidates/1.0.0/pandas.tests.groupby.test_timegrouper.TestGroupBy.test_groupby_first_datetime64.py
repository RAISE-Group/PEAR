def test_groupby_first_datetime64(self):
    df = DataFrame([(1, 1351036800000000000), (2, 1351036800000000000)])
    df[1] = df[1].view('M8[ns]')
    assert issubclass(df[1].dtype.type, np.datetime64)
    result = df.groupby(level=0).first()
    got_dt = result[1].dtype
    assert issubclass(got_dt.type, np.datetime64)
    result = df[1].groupby(level=0).first()
    got_dt = result.dtype
    assert issubclass(got_dt.type, np.datetime64)