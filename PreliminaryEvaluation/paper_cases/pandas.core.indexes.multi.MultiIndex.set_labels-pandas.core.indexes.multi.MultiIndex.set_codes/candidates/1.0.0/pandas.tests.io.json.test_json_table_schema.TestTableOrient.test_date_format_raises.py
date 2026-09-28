def test_date_format_raises(self):
    with pytest.raises(ValueError):
        self.df.to_json(orient='table', date_format='epoch')
    self.df.to_json(orient='table', date_format='iso')
    self.df.to_json(orient='table')