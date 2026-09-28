def test_drop_dst_boundary(self):
    tz = 'Europe/Brussels'
    freq = '15min'
    start = pd.Timestamp('201710290100', tz=tz)
    end = pd.Timestamp('201710290300', tz=tz)
    index = pd.date_range(start=start, end=end, freq=freq)
    expected = DatetimeIndex(['201710290115', '201710290130', '201710290145', '201710290200', '201710290215', '201710290230', '201710290245', '201710290200', '201710290215', '201710290230', '201710290245', '201710290300'], tz=tz, freq=freq, ambiguous=[True, True, True, True, True, True, True, False, False, False, False, False])
    result = index.drop(index[0])
    tm.assert_index_equal(result, expected)