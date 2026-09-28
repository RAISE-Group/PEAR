def test_generator_warnings(self):
    sp_arr = SparseArray([1, 2, 3])
    with warnings.catch_warnings(record=True) as w:
        warnings.filterwarnings(action='always', category=DeprecationWarning)
        warnings.filterwarnings(action='always', category=PendingDeprecationWarning)
        for _ in sp_arr:
            pass
        assert len(w) == 0