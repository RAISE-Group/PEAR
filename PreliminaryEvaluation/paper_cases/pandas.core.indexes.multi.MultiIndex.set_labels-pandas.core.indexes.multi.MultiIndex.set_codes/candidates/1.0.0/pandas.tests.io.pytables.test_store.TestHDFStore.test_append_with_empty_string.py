def test_append_with_empty_string(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = DataFrame({'x': ['a', 'b', 'c', 'd', 'e', 'f', '']})
        store.append('df', df[:-1], min_itemsize={'x': 1})
        store.append('df', df[-1:], min_itemsize={'x': 1})
        tm.assert_frame_equal(store.select('df'), df)