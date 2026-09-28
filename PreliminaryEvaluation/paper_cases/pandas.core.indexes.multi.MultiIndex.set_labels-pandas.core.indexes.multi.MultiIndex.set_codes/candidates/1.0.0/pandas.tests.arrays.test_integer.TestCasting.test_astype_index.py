@pytest.mark.parametrize('dropna', [True, False])
def test_astype_index(self, all_data, dropna):
    all_data = all_data[:10]
    if dropna:
        other = all_data[~all_data.isna()]
    else:
        other = all_data
    dtype = all_data.dtype
    idx = pd.Index(np.array(other))
    assert isinstance(idx, ABCIndexClass)
    result = idx.astype(dtype)
    expected = idx.astype(object).astype(dtype)
    tm.assert_index_equal(result, expected)