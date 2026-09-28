def test_iter(self):
    strs = ('google', 'wikimedia', 'wikipedia', 'wikitravel')
    ds = Series(strs)
    with tm.assert_produces_warning(FutureWarning):
        for s in ds.str:
            assert isinstance(s, Series)
            tm.assert_index_equal(s.index, ds.index)
            for el in s:
                assert isinstance(el, str) or isna(el)
    assert s.dropna().values.item() == 'l'