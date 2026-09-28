def test_query_long_float_literal(self, setup_path):
    df = pd.DataFrame({'A': [1000000000.0009, 1000000000.0011, 1000000000.0015]})
    with ensure_clean_store(setup_path) as store:
        store.append('test', df, format='table', data_columns=True)
        cutoff = 1000000000.0006
        result = store.select('test', 'A < {cutoff:.4f}'.format(cutoff=cutoff))
        assert result.empty
        cutoff = 1000000000.001
        result = store.select('test', 'A > {cutoff:.4f}'.format(cutoff=cutoff))
        expected = df.loc[[1, 2], :]
        tm.assert_frame_equal(expected, result)
        exact = 1000000000.0011
        result = store.select('test', 'A == {exact:.4f}'.format(exact=exact))
        expected = df.loc[[1], :]
        tm.assert_frame_equal(expected, result)