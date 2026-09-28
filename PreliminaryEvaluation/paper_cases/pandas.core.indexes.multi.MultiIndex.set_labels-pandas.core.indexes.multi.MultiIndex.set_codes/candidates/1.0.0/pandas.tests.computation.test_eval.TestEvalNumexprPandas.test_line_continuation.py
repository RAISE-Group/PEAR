def test_line_continuation(self):
    exp = '1 + 2 *         5 - 1 + 2 '
    result = pd.eval(exp, engine=self.engine, parser=self.parser)
    assert result == 12