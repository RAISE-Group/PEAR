@pytest.mark.parametrize('box', [np.array, Series, list])
@pytest.mark.parametrize('sort', [None, False])
def test_union3(self, sort, box):
    everything = tm.makeDateIndex(10)
    first = everything[:5]
    second = everything[5:]
    expected = first.astype('O').union(pd.Index(second.values, dtype='O')).astype('O')
    case = box(second.values)
    result = first.union(case, sort=sort)
    tm.assert_index_equal(result, expected)