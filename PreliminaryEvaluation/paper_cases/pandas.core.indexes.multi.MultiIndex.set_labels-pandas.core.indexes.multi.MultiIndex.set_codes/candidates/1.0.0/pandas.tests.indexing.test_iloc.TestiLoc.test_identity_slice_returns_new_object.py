def test_identity_slice_returns_new_object(self):
    original_df = DataFrame({'a': [1, 2, 3]})
    sliced_df = original_df.iloc[:]
    assert sliced_df is not original_df
    original_df['a'] = [4, 4, 4]
    assert (sliced_df['a'] == 4).all()
    original_series = Series([1, 2, 3, 4, 5, 6])
    sliced_series = original_series.iloc[:]
    assert sliced_series is not original_series
    original_series[:3] = [7, 8, 9]
    assert all(sliced_series[:3] == [7, 8, 9])