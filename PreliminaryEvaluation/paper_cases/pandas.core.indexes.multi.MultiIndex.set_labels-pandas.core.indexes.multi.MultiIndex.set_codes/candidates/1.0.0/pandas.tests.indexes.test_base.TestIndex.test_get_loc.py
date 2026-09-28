@pytest.mark.parametrize('method', [None, 'pad', 'backfill', 'nearest'])
def test_get_loc(self, method):
    index = pd.Index([0, 1, 2])
    assert index.get_loc(1, method=method) == 1
    if method:
        assert index.get_loc(1, method=method, tolerance=0) == 1