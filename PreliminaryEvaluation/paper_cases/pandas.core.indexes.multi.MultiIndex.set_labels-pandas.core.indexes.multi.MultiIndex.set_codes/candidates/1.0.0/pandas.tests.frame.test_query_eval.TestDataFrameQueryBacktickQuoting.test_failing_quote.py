def test_failing_quote(self, df):
    with pytest.raises(SyntaxError):
        df.query("`it's` > `that's`")