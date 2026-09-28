def test_spam_header(self):
    df = self.read_html(self.spam_data, '.*Water.*', header=2)[0]
    assert df.columns[0] == 'Proximates'
    assert not df.empty