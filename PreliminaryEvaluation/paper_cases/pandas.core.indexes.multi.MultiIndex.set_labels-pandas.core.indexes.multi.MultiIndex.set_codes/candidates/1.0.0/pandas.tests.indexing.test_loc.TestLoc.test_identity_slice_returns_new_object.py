def test_identity_slice_returns_new_object(self):
    original_df = DataFrame({'a': [1, 2, 3]})
    sliced_df = original_df.loc[:]
    assert sliced_df is not original_df
    assert original_df[:] is not original_df
    original_df['a'] = [4, 4, 4]
    assert (sliced_df['a'] == 4).all()
    assert original_df is original_df.loc[:, :]
    df = DataFrame(np.random.randn(10, 4))
    assert df[0] is df.loc[:, 0]
    original_series = Series([1, 2, 3, 4, 5, 6])
    sliced_series = original_series.loc[:]
    assert sliced_series is not original_series
    assert original_series[:] is not original_series
    original_series[:3] = [7, 8, 9]
    assert all(sliced_series[:3] == [7, 8, 9])