@pytest.mark.slow
def test_fallback_success(self, datapath):
    banklist_data = datapath('io', 'data', 'html', 'banklist.html')
    self.read_html(banklist_data, '.*Water.*', flavor=['lxml', 'html5lib'])