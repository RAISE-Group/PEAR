@pytest.mark.parametrize('table_format', ['table', 'fixed'])
def test_store_index_name_numpy_str(self, table_format, setup_path):
    idx = pd.Index(pd.to_datetime([datetime.date(2000, 1, 1), datetime.date(2000, 1, 2)]), name='colsג')
    idx1 = pd.Index(pd.to_datetime([datetime.date(2010, 1, 1), datetime.date(2010, 1, 2)]), name='rowsא')
    df = pd.DataFrame(np.arange(4).reshape(2, 2), columns=idx, index=idx1)
    with ensure_clean_path(setup_path) as path:
        df.to_hdf(path, 'df', format=table_format)
        df2 = read_hdf(path, 'df')
        tm.assert_frame_equal(df, df2, check_names=True)
        assert type(df2.index.name) == str
        assert type(df2.columns.name) == str