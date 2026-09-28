def test_rename_with_custom_indexer_inplace(self):

    class MyIndexer:
        pass
    ix = MyIndexer()
    s = Series([1, 2, 3])
    s.rename(ix, inplace=True)
    assert s.name is ix