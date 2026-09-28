def test_tab_completion_with_categorical(self):
    ok_for_cat = ['categories', 'codes', 'ordered', 'set_categories', 'add_categories', 'remove_categories', 'rename_categories', 'reorder_categories', 'remove_unused_categories', 'as_ordered', 'as_unordered']

    def get_dir(s):
        results = [r for r in s.cat.__dir__() if not r.startswith('_')]
        return sorted(set(results))
    s = Series(list('aabbcde')).astype('category')
    results = get_dir(s)
    tm.assert_almost_equal(results, sorted(set(ok_for_cat)))