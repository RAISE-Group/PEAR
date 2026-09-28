def test_reindex_preserves_tz_if_target_is_empty_list_or_array(self):
    index = date_range('20130101', periods=3, tz='US/Eastern')
    assert str(index.reindex([])[0].tz) == 'US/Eastern'
    assert str(index.reindex(np.array([]))[0].tz) == 'US/Eastern'