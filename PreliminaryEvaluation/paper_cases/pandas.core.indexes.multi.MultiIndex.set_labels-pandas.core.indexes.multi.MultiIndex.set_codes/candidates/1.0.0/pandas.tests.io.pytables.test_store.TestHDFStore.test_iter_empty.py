def test_iter_empty(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        assert list(store) == []