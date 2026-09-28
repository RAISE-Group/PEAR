def test_set(self):
    mgr = create_mgr('a,b,c: int', item_shape=(3,))
    mgr.set('d', np.array(['foo'] * 3))
    mgr.set('b', np.array(['bar'] * 3))
    tm.assert_numpy_array_equal(mgr.get('a').internal_values(), np.array([0] * 3))
    tm.assert_numpy_array_equal(mgr.get('b').internal_values(), np.array(['bar'] * 3, dtype=np.object_))
    tm.assert_numpy_array_equal(mgr.get('c').internal_values(), np.array([2] * 3))
    tm.assert_numpy_array_equal(mgr.get('d').internal_values(), np.array(['foo'] * 3, dtype=np.object_))