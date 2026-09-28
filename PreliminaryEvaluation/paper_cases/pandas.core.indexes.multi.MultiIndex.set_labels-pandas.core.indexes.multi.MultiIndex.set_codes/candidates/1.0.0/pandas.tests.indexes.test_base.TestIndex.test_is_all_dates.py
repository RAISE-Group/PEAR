@pytest.mark.parametrize('index, expected', [('string', False), ('bool', False), ('categorical', False), ('int', False), ('datetime', True), ('float', False)], indirect=['index'])
def test_is_all_dates(self, index, expected):
    assert index.is_all_dates is expected