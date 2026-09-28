def test_reindex_items(self):
    mgr = create_mgr('a: f8; b: i8; c: f8; d: i8; e: f8; f: bool; g: f8-2')
    reindexed = mgr.reindex_axis(['g', 'c', 'a', 'd'], axis=0)
    assert reindexed.nblocks == 2
    tm.assert_index_equal(reindexed.items, pd.Index(['g', 'c', 'a', 'd']))
    tm.assert_almost_equal(mgr.get('g').internal_values(), reindexed.get('g').internal_values())
    tm.assert_almost_equal(mgr.get('c').internal_values(), reindexed.get('c').internal_values())
    tm.assert_almost_equal(mgr.get('a').internal_values(), reindexed.get('a').internal_values())
    tm.assert_almost_equal(mgr.get('d').internal_values(), reindexed.get('d').internal_values())