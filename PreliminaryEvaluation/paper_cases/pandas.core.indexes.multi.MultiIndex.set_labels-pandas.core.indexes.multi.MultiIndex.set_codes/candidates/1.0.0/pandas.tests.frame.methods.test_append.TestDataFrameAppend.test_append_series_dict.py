def test_append_series_dict(self):
    df = DataFrame(np.random.randn(5, 4), columns=['foo', 'bar', 'baz', 'qux'])
    series = df.loc[4]
    msg = 'Indexes have overlapping values'
    with pytest.raises(ValueError, match=msg):
        df.append(series, verify_integrity=True)
    series.name = None
    msg = 'Can only append a Series if ignore_index=True'
    with pytest.raises(TypeError, match=msg):
        df.append(series, verify_integrity=True)
    result = df.append(series[::-1], ignore_index=True)
    expected = df.append(DataFrame({0: series[::-1]}, index=df.columns).T, ignore_index=True)
    tm.assert_frame_equal(result, expected)
    result = df.append(series.to_dict(), ignore_index=True)
    tm.assert_frame_equal(result, expected)
    result = df.append(series[::-1][:3], ignore_index=True)
    expected = df.append(DataFrame({0: series[::-1][:3]}).T, ignore_index=True, sort=True)
    tm.assert_frame_equal(result, expected.loc[:, result.columns])
    row = df.loc[4]
    row.name = 5
    result = df.append(row)
    expected = df.append(df[-1:], ignore_index=True)
    tm.assert_frame_equal(result, expected)