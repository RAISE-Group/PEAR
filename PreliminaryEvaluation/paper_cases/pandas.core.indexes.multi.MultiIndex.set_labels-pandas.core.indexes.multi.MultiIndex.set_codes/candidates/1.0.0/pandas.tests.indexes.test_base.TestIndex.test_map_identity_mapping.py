def test_map_identity_mapping(self, indices):
    tm.assert_index_equal(indices, indices.map(lambda x: x))