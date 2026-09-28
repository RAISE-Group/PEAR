def test_table_index_incompatible_dtypes(self, setup_path):
    df1 = DataFrame({'a': [1, 2, 3]})
    df2 = DataFrame({'a': [4, 5, 6]}, index=date_range('1/1/2000', periods=3))
    with ensure_clean_store(setup_path) as store:
        store.put('frame', df1, format='table')
        with pytest.raises(TypeError):
            store.put('frame', df2, format='table', append=True)