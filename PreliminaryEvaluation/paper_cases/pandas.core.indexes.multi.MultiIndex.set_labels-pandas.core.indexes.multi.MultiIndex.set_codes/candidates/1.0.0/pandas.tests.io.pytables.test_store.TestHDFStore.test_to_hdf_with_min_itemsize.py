def test_to_hdf_with_min_itemsize(self, setup_path):
    with ensure_clean_path(setup_path) as path:
        df = tm.makeMixedDataFrame().set_index('C')
        df.to_hdf(path, 'ss3', format='table', min_itemsize={'index': 6})
        df2 = df.copy().reset_index().assign(C='longer').set_index('C')
        df2.to_hdf(path, 'ss3', append=True, format='table')
        tm.assert_frame_equal(pd.read_hdf(path, 'ss3'), pd.concat([df, df2]))
        df['B'].to_hdf(path, 'ss4', format='table', min_itemsize={'index': 6})
        df2['B'].to_hdf(path, 'ss4', append=True, format='table')
        tm.assert_series_equal(pd.read_hdf(path, 'ss4'), pd.concat([df['B'], df2['B']]))