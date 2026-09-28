def test_negative_skiprows(self):
    msg = '\\(you passed a negative value\\)'
    with pytest.raises(ValueError, match=msg):
        self.read_html(self.spam_data, 'Water', skiprows=-1)