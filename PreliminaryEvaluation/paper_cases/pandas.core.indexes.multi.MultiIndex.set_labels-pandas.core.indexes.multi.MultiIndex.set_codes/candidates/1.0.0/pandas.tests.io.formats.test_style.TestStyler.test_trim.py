def test_trim(self):
    result = self.df.style.render()
    assert result.count('#') == 0
    result = self.df.style.highlight_max().render()
    assert result.count('#') == len(self.df.columns)