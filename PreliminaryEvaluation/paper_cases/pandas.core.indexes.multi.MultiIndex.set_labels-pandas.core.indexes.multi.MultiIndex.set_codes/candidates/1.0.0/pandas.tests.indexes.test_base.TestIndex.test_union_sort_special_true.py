@pytest.mark.xfail(reason='Not implemented')
@pytest.mark.parametrize('slice_', [slice(None), slice(0)])
def test_union_sort_special_true(self, slice_):
    idx = pd.Index([1, 0, 2])
    other = idx[slice_]
    result = idx.union(other, sort=True)
    expected = pd.Index([0, 1, 2])
    tm.assert_index_equal(result, expected)