@pytest.mark.parametrize('column', ['ms', 'day', 'week', 'month', 'qtr', 'half', 'yr'])
def test_date_parsing_ignores_format_details(self, column):
    df = read_stata(self.stata_dates)
    unformatted = df.loc[0, column]
    formatted = df.loc[0, column + '_fmt']
    assert unformatted == formatted