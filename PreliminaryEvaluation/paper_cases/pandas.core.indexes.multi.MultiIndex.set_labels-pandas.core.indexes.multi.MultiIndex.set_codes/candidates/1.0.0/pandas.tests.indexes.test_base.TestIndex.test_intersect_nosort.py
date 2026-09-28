def test_intersect_nosort(self):
    result = pd.Index(['c', 'b', 'a']).intersection(['b', 'a'])
    expected = pd.Index(['b', 'a'])
    tm.assert_index_equal(result, expected)