def test_view(self, indices):
    assert indices.view().name == indices.name