def test_to_html(self):
    self.ymd.columns.name = 'foo'
    self.ymd.to_html()
    self.ymd.T.to_html()