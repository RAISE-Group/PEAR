@pytest.mark.parametrize('index', ['unicode', 'string', 'datetime', 'int', 'float'], indirect=True)
def test_join_self(self, index, join_type):
    joined = index.join(index, how=join_type)
    assert index is joined