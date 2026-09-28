def test_copy_blocks(self, float_frame):
    df = DataFrame(float_frame, copy=True)
    column = df.columns[0]
    blocks = df._to_dict_of_blocks(copy=True)
    for dtype, _df in blocks.items():
        if column in _df:
            _df.loc[:, column] = _df[column] + 1
    assert not _df[column].equals(df[column])