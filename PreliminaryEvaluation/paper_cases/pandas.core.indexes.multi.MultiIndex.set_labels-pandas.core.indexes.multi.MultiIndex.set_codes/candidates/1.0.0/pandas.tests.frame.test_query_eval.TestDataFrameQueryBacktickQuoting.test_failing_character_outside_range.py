def test_failing_character_outside_range(self, df):
    with pytest.raises(SyntaxError):
        df.query('`☺` > 4')