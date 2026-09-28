def test_drop_duplicates_metadata(self):
    idx = pd.timedelta_range('1 day', '31 day', freq='D', name='idx')
    result = idx.drop_duplicates()
    tm.assert_index_equal(idx, result)
    assert idx.freq == result.freq
    idx_dup = idx.append(idx)
    assert idx_dup.freq is None
    result = idx_dup.drop_duplicates()
    tm.assert_index_equal(idx, result)
    assert result.freq is None