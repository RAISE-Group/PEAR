def test_join_with_len0(self):
    merged = self.target.join(self.source.reindex([]), on='C')
    for col in self.source:
        assert col in merged
        assert merged[col].isna().all()
    merged2 = self.target.join(self.source.reindex([]), on='C', how='inner')
    tm.assert_index_equal(merged2.columns, merged.columns)
    assert len(merged2) == 0