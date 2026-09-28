def test_set_frame_overwrite_object(self, data):
    df = pd.DataFrame({'A': [1] * len(data)}, dtype=object)
    df['A'] = data
    assert df.dtypes['A'] == data.dtype