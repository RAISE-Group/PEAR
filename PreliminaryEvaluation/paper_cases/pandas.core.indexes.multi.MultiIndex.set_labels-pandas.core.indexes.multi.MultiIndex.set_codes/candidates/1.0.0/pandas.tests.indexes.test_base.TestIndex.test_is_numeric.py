@pytest.mark.parametrize('index, expected', [('string', False), ('bool', False), ('categorical', False), ('int', True), ('datetime', False), ('float', True)], indirect=['index'])
def test_is_numeric(self, index, expected):
    assert index.is_numeric() is expected