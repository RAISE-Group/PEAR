@pytest.mark.parametrize('method', ['pad', 'backfill', 'nearest'])
def test_get_loc_outside_tolerance_raises(self, method):
    index = pd.Index([0, 1, 2])
    with pytest.raises(KeyError, match='1.1'):
        index.get_loc(1.1, method, tolerance=0.05)