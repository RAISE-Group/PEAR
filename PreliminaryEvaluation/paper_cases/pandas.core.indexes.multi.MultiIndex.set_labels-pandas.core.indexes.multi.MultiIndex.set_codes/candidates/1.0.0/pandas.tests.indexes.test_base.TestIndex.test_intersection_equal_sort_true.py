@pytest.mark.xfail(reason='Not implemented')
def test_intersection_equal_sort_true(self):
    idx = pd.Index(['c', 'a', 'b'])
    sorted_ = pd.Index(['a', 'b', 'c'])
    tm.assert_index_equal(idx.intersection(idx, sort=True), sorted_)