def test_data_frame_size_after_to_json(self):
    df = DataFrame({'a': [str(1)]})
    size_before = df.memory_usage(index=True, deep=True).sum()
    df.to_json()
    size_after = df.memory_usage(index=True, deep=True).sum()
    assert size_before == size_after