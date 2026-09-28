def test_iter_object_try_string(self):
    ds = Series([slice(None, randint(10), randint(10, 20)) for _ in range(4)])
    i, s = (100, 'h')
    with tm.assert_produces_warning(FutureWarning):
        for i, s in enumerate(ds.str):
            pass
    assert i == 100
    assert s == 'h'