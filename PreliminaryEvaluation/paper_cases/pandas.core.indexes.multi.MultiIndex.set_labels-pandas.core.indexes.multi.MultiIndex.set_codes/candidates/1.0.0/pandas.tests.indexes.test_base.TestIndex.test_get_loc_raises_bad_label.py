@pytest.mark.parametrize('method', [None, 'pad', 'backfill', 'nearest'])
def test_get_loc_raises_bad_label(self, method):
    index = pd.Index([0, 1, 2])
    if method:
        msg = 'not supported between'
    else:
        msg = 'invalid key'
    with pytest.raises(TypeError, match=msg):
        index.get_loc([1, 2], method=method)