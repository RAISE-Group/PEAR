def test_categorical_conversion(self, setup_path):
    obsids = ['ESP_012345_6789', 'ESP_987654_3210']
    imgids = ['APF00006np', 'APF0001imm']
    data = [4.3, 9.8]
    df = DataFrame(dict(obsids=obsids, imgids=imgids, data=data))
    expected = df.iloc[[], :]
    with ensure_clean_path(setup_path) as path:
        df.to_hdf(path, 'df', format='table', data_columns=True)
        result = read_hdf(path, 'df', where='obsids=B')
        tm.assert_frame_equal(result, expected)
    df.obsids = df.obsids.astype('category')
    df.imgids = df.imgids.astype('category')
    expected = df.iloc[[], :]
    with ensure_clean_path(setup_path) as path:
        df.to_hdf(path, 'df', format='table', data_columns=True)
        result = read_hdf(path, 'df', where='obsids=B')
        tm.assert_frame_equal(result, expected)