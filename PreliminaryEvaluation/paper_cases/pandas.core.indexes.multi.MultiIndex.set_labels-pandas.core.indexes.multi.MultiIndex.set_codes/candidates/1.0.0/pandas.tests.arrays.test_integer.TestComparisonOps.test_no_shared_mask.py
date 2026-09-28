def test_no_shared_mask(self, data):
    result = data + 1
    assert np.shares_memory(result._mask, data._mask) is False