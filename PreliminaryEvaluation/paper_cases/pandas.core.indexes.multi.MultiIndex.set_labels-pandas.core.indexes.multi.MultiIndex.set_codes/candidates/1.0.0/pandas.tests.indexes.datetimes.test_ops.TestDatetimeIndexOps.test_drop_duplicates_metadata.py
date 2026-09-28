def test_drop_duplicates_metadata(self):
    idx = pd.date_range('2011-01-01', '2011-01-31', freq='D', name='idx')
    result = idx.drop_duplicates()
    tm.assert_index_equal(idx, result)
    assert idx.freq == result.freq
    idx_dup = idx.append(idx)
    assert idx_dup.freq is None
    result = idx_dup.drop_duplicates()
    tm.assert_index_equal(idx, result)
    assert result.freq is None