@pytest.mark.parametrize('orient,expected', [('index', '{"(\'a\', \'b\')":{"(\'c\', \'d\')":1}}'), ('columns', '{"(\'c\', \'d\')":{"(\'a\', \'b\')":1}}'), pytest.param('split', '', marks=pytest.mark.skip), pytest.param('table', '', marks=pytest.mark.skip)])
def test_tuple_labels(self, orient, expected):
    df = pd.DataFrame([[1]], index=[('a', 'b')], columns=[('c', 'd')])
    result = df.to_json(orient=orient)
    assert result == expected