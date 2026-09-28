@pytest.mark.parametrize('protocol', [-1, 0, 1, 2])
def test_read(self, protocol, get_random_path):
    with tm.ensure_clean(get_random_path) as path:
        df = tm.makeDataFrame()
        df.to_pickle(path, protocol=protocol)
        df2 = pd.read_pickle(path)
        tm.assert_frame_equal(df, df2)