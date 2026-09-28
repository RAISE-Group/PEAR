def test_create_table_index(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        with catch_warnings(record=True):

            def col(t, column):
                return getattr(store.get_storer(t).table.cols, column)
            df = tm.makeTimeDataFrame()
            df['string'] = 'foo'
            df['string2'] = 'bar'
            store.append('f', df, data_columns=['string', 'string2'])
            assert col('f', 'index').is_indexed is True
            assert col('f', 'string').is_indexed is True
            assert col('f', 'string2').is_indexed is True
            store.append('f2', df, index=['string'], data_columns=['string', 'string2'])
            assert col('f2', 'index').is_indexed is False
            assert col('f2', 'string').is_indexed is True
            assert col('f2', 'string2').is_indexed is False
            _maybe_remove(store, 'f2')
            store.put('f2', df)
            with pytest.raises(TypeError):
                store.create_table_index('f2')