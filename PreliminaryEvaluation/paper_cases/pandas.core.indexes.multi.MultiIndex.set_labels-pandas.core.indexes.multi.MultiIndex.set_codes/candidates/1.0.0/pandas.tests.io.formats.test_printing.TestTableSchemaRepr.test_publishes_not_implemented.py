def test_publishes_not_implemented(self):
    midx = pd.MultiIndex.from_product([['A', 'B'], ['a', 'b', 'c']])
    df = pd.DataFrame(np.random.randn(5, len(midx)), columns=midx)
    opt = pd.option_context('display.html.table_schema', True)
    with opt:
        formatted = self.display_formatter.format(df)
    expected = {'text/plain', 'text/html'}
    assert set(formatted[0].keys()) == expected