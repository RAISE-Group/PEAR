@tm.network
def test_read_from_http_url(self, read_ext):
    url = 'https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/io/data/excel/test1' + read_ext
    url_table = pd.read_excel(url)
    local_table = pd.read_excel('test1' + read_ext)
    tm.assert_frame_equal(url_table, local_table)