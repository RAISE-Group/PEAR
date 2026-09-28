@tm.network
@pytest.mark.slow
def test_invalid_url(self):
    try:
        with pytest.raises(URLError):
            self.read_html('http://www.a23950sdfa908sd.com', match='.*Water.*')
    except ValueError as e:
        assert 'No tables found' in str(e)