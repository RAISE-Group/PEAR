def test_equals_block_order_different_dtypes(self):
    mgr_strings = ['a:i8;b:f8', 'a:i8;b:f8;c:c8;d:b', 'a:i8;e:dt;f:td;g:string', 'a:i8;b:category;c:category2;d:category2', 'c:sparse;d:sparse_na;b:f8']
    for mgr_string in mgr_strings:
        bm = create_mgr(mgr_string)
        block_perms = itertools.permutations(bm.blocks)
        for bm_perm in block_perms:
            bm_this = BlockManager(bm_perm, bm.axes)
            assert bm.equals(bm_this)
            assert bm_this.equals(bm)