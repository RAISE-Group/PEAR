def test_logical_compat(self):
    idx = self.create_index()
    with pytest.raises(TypeError, match='cannot perform all'):
        idx.all()
    with pytest.raises(TypeError, match='cannot perform any'):
        idx.any()