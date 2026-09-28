@pytest.mark.slow
@pytest.mark.filterwarnings('ignore:This metho:PendingDeprecationWarning')
def test_read_from_file_url(self, read_ext, datapath):
    localtable = os.path.join(datapath('io', 'data', 'excel'), 'test1' + read_ext)
    local_table = pd.read_excel(localtable)
    try:
        url_table = pd.read_excel('file://localhost/' + localtable)
    except URLError:
        import platform
        pytest.skip('failing on {}'.format(' '.join(platform.uname()).strip()))
    tm.assert_frame_equal(url_table, local_table)