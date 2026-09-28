@pytest.mark.parametrize('where, expected', [('/', {'': ({'first_group', 'second_group'}, set()), '/first_group': (set(), {'df1', 'df2'}), '/second_group': ({'third_group'}, {'df3', 's1'}), '/second_group/third_group': (set(), {'df4'})}), ('/second_group', {'/second_group': ({'third_group'}, {'df3', 's1'}), '/second_group/third_group': (set(), {'df4'})})])
def test_walk(self, where, expected, setup_path):
    objs = {'df1': pd.DataFrame([1, 2, 3]), 'df2': pd.DataFrame([4, 5, 6]), 'df3': pd.DataFrame([6, 7, 8]), 'df4': pd.DataFrame([9, 10, 11]), 's1': pd.Series([10, 9, 8]), 'a1': np.array([[1, 2, 3], [4, 5, 6]]), 'tb1': np.array([(1, 2, 3), (4, 5, 6)], dtype='i,i,i'), 'tb2': np.array([(7, 8, 9), (10, 11, 12)], dtype='i,i,i')}
    with ensure_clean_store('walk_groups.hdf', mode='w') as store:
        store.put('/first_group/df1', objs['df1'])
        store.put('/first_group/df2', objs['df2'])
        store.put('/second_group/df3', objs['df3'])
        store.put('/second_group/s1', objs['s1'])
        store.put('/second_group/third_group/df4', objs['df4'])
        store._handle.create_array('/first_group', 'a1', objs['a1'])
        store._handle.create_table('/first_group', 'tb1', obj=objs['tb1'])
        store._handle.create_table('/second_group', 'tb2', obj=objs['tb2'])
        assert len(list(store.walk(where=where))) == len(expected)
        for path, groups, leaves in store.walk(where=where):
            assert path in expected
            expected_groups, expected_frames = expected[path]
            assert expected_groups == set(groups)
            assert expected_frames == set(leaves)
            for leaf in leaves:
                frame_path = '/'.join([path, leaf])
                obj = store.get(frame_path)
                if 'df' in leaf:
                    tm.assert_frame_equal(obj, objs[leaf])
                else:
                    tm.assert_series_equal(obj, objs[leaf])