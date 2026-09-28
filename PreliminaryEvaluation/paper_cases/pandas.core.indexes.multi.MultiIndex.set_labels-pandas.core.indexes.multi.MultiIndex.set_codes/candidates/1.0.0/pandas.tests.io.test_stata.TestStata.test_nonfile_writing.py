@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
def test_nonfile_writing(self, version):
    bio = io.BytesIO()
    df = tm.makeDataFrame()
    df.index.name = 'index'
    with tm.ensure_clean() as path:
        df.to_stata(bio, version=version)
        bio.seek(0)
        with open(path, 'wb') as dta:
            dta.write(bio.read())
        reread = pd.read_stata(path, index_col='index')
    tm.assert_frame_equal(df, reread)