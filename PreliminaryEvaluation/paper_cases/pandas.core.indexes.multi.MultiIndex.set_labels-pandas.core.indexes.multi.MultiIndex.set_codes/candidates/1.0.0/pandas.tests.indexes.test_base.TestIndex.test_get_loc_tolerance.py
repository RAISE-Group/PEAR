@pytest.mark.parametrize('method,loc', [('pad', 1), ('backfill', 2), ('nearest', 1)])
def test_get_loc_tolerance(self, method, loc):
    index = pd.Index([0, 1, 2])
    assert index.get_loc(1.1, method) == loc
    assert index.get_loc(1.1, method, tolerance=1) == loc