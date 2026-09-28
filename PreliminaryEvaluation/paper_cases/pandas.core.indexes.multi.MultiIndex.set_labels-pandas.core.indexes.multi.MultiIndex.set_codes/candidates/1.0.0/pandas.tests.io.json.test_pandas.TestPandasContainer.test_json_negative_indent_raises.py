def test_json_negative_indent_raises(self):
    with pytest.raises(ValueError, match='must be a nonnegative integer'):
        pd.DataFrame().to_json(indent=-1)