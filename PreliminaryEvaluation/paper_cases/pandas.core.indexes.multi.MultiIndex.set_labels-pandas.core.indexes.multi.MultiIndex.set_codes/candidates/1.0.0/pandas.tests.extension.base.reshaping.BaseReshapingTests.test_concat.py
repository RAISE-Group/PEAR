@pytest.mark.parametrize('in_frame', [True, False])
def test_concat(self, data, in_frame):
    wrapped = pd.Series(data)
    if in_frame:
        wrapped = pd.DataFrame(wrapped)
    result = pd.concat([wrapped, wrapped], ignore_index=True)
    assert len(result) == len(data) * 2
    if in_frame:
        dtype = result.dtypes[0]
    else:
        dtype = result.dtype
    assert dtype == data.dtype
    assert isinstance(result._data.blocks[0], ExtensionBlock)