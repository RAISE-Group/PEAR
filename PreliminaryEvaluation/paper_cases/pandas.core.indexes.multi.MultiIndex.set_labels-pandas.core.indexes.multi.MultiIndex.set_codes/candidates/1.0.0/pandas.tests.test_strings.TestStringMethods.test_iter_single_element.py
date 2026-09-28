def test_iter_single_element(self):
    ds = Series(['a'])
    with tm.assert_produces_warning(FutureWarning):
        for i, s in enumerate(ds.str):
            pass
    assert not i
    tm.assert_series_equal(ds, s)