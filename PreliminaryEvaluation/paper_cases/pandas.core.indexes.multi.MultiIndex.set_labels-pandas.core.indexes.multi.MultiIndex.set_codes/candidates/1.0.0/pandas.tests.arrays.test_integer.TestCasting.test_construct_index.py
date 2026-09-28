@pytest.mark.parametrize('dropna', [True, False])
def test_construct_index(self, all_data, dropna):
    all_data = all_data[:10]
    if dropna:
        other = np.array(all_data[~all_data.isna()])
    else:
        other = all_data
    result = pd.Index(integer_array(other, dtype=all_data.dtype))
    expected = pd.Index(other, dtype=object)
    tm.assert_index_equal(result, expected)