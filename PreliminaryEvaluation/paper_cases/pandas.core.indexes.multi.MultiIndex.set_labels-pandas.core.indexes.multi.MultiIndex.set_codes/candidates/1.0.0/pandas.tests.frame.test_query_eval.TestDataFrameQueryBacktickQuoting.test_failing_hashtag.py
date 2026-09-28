def test_failing_hashtag(self, df):
    with pytest.raises(SyntaxError):
        df.query('`foo#bar` > 4')