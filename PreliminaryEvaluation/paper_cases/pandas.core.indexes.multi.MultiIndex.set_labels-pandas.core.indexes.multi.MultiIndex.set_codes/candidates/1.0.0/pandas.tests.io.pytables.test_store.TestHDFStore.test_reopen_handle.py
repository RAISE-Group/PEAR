def test_reopen_handle(self, setup_path):
    with ensure_clean_path(setup_path) as path:
        store = HDFStore(path, mode='a')
        store['a'] = tm.makeTimeSeries()
        with pytest.raises(PossibleDataLossError):
            store.open('w')
        store.close()
        assert not store.is_open
        store.open('w')
        assert store.is_open
        assert len(store) == 0
        store.close()
        assert not store.is_open
        store = HDFStore(path, mode='a')
        store['a'] = tm.makeTimeSeries()
        store.open('r')
        assert store.is_open
        assert len(store) == 1
        assert store._mode == 'r'
        store.close()
        assert not store.is_open
        store.open('a')
        assert store.is_open
        assert len(store) == 1
        assert store._mode == 'a'
        store.close()
        assert not store.is_open
        store.open('a')
        assert store.is_open
        assert len(store) == 1
        assert store._mode == 'a'
        store.close()
        assert not store.is_open