def test_query_compare_column_type(self, setup_path):
    df = pd.DataFrame({'date': ['2014-01-01', '2014-01-02'], 'real_date': date_range('2014-01-01', periods=2), 'float': [1.1, 1.2], 'int': [1, 2]}, columns=['date', 'real_date', 'float', 'int'])
    with ensure_clean_store(setup_path) as store:
        store.append('test', df, format='table', data_columns=True)
        ts = pd.Timestamp('2014-01-01')
        result = store.select('test', where='real_date > ts')
        expected = df.loc[[1], :]
        tm.assert_frame_equal(expected, result)
        for op in ['<', '>', '==']:
            for v in [2.1, True, pd.Timestamp('2014-01-01'), pd.Timedelta(1, 's')]:
                query = 'date {op} v'.format(op=op)
                with pytest.raises(TypeError):
                    store.select('test', where=query)
            v = 'a'
            for col in ['int', 'float', 'real_date']:
                query = '{col} {op} v'.format(op=op, col=col)
                with pytest.raises(ValueError):
                    store.select('test', where=query)
            for v, col in zip(['1', '1.1', '2014-01-01'], ['int', 'float', 'real_date']):
                query = '{col} {op} v'.format(op=op, col=col)
                result = store.select('test', where=query)
                if op == '==':
                    expected = df.loc[[0], :]
                elif op == '>':
                    expected = df.loc[[1], :]
                else:
                    expected = df.loc[[], :]
                tm.assert_frame_equal(expected, result)