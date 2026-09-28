def test_top_level_method(self):
    result = melt(self.df)
    assert result.columns.tolist() == ['variable', 'value']