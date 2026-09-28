def test_iter_empty(self):
    ds = Series([], dtype=object)
    i, s = (100, 1)
    with tm.assert_produces_warning(FutureWarning):
        for i, s in enumerate(ds.str):
            pass
    assert i == 100
    assert s == 1