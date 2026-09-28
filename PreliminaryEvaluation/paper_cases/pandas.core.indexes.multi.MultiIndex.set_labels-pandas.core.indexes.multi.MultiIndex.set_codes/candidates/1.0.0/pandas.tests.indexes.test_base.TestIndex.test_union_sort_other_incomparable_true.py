@pytest.mark.xfail(reason='Not implemented')
def test_union_sort_other_incomparable_true(self):
    idx = pd.Index([1, pd.Timestamp('2000')])
    with pytest.raises(TypeError, match='.*'):
        idx.union(idx[:1], sort=True)