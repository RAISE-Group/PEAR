@pytest.mark.parametrize('index, expected', [('string', True), ('bool', True), ('categorical', False), ('int', False), ('datetime', False), ('float', False)], indirect=['index'])
def test_is_object(self, index, expected):
    assert index.is_object() is expected