def test_to_flat_index(self, indices):
    if isinstance(indices, MultiIndex):
        pytest.skip('Separate expectation for MultiIndex')
    result = indices.to_flat_index()
    tm.assert_index_equal(result, indices)