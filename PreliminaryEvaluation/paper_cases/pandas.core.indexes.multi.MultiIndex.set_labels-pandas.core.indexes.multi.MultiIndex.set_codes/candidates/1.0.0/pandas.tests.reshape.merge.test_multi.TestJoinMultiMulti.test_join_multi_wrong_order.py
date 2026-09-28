def test_join_multi_wrong_order(self):
    midx1 = pd.MultiIndex.from_product([[1, 2], [3, 4]], names=['a', 'b'])
    midx3 = pd.MultiIndex.from_tuples([(4, 1), (3, 2), (3, 1)], names=['b', 'a'])
    left = pd.DataFrame(index=midx1, data={'x': [10, 20, 30, 40]})
    right = pd.DataFrame(index=midx3, data={'y': ['foo', 'bar', 'fing']})
    result = left.join(right)
    expected = pd.DataFrame(index=midx1, data={'x': [10, 20, 30, 40], 'y': ['fing', 'foo', 'bar', np.nan]})
    tm.assert_frame_equal(result, expected)