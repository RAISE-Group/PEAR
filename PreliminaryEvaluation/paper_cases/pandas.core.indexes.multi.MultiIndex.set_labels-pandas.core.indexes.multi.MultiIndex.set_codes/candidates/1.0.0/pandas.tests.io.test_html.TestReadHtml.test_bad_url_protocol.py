@tm.network
def test_bad_url_protocol(self):
    with pytest.raises(URLError):
        self.read_html('git://github.com', match='.*Water.*')