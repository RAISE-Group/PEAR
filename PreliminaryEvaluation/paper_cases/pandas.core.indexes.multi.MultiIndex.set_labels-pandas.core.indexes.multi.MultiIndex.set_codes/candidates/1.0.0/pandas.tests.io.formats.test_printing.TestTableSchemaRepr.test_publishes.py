def test_publishes(self):
    df = pd.DataFrame({'A': [1, 2]})
    objects = [df['A'], df, df]
    expected_keys = [{'text/plain', 'application/vnd.dataresource+json'}, {'text/plain', 'text/html', 'application/vnd.dataresource+json'}]
    opt = pd.option_context('display.html.table_schema', True)
    for obj, expected in zip(objects, expected_keys):
        with opt:
            formatted = self.display_formatter.format(obj)
        assert set(formatted[0].keys()) == expected
    with_latex = pd.option_context('display.latex.repr', True)
    with opt, with_latex:
        formatted = self.display_formatter.format(obj)
    expected = {'text/plain', 'text/html', 'text/latex', 'application/vnd.dataresource+json'}
    assert set(formatted[0].keys()) == expected