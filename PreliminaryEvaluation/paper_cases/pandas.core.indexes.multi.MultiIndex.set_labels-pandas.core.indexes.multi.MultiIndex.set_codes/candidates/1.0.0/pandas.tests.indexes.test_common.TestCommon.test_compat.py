def test_compat(self, indices):
    assert indices.tolist() == list(indices)