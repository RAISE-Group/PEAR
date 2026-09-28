def test_append_with_diff_col_name_types_raises_value_error(self, setup_path):
    df = DataFrame(np.random.randn(10, 1))
    df2 = DataFrame({'a': np.random.randn(10)})
    df3 = DataFrame({(1, 2): np.random.randn(10)})
    df4 = DataFrame({('1', 2): np.random.randn(10)})
    df5 = DataFrame({('1', 2, object): np.random.randn(10)})
    with ensure_clean_store(setup_path) as store:
        name = 'df_{}'.format(tm.rands(10))
        store.append(name, df)
        for d in (df2, df3, df4, df5):
            with pytest.raises(ValueError):
                store.append(name, d)