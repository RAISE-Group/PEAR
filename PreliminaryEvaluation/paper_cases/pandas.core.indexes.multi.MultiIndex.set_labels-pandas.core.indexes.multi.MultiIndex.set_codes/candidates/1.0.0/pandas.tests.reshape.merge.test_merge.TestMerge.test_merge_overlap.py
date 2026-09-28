def test_merge_overlap(self):
    merged = merge(self.left, self.left, on='key')
    exp_len = (self.left['key'].value_counts() ** 2).sum()
    assert len(merged) == exp_len
    assert 'v1_x' in merged
    assert 'v1_y' in merged