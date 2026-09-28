def test_engine_reference_cycle(self):
    index = self.create_index()
    nrefs_pre = len(gc.get_referrers(index))
    index._engine
    assert len(gc.get_referrers(index)) == nrefs_pre