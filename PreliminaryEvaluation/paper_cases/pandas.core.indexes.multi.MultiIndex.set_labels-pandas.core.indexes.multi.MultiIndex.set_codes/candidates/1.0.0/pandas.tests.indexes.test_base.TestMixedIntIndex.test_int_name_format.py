@pytest.mark.parametrize('klass', [Series, DataFrame])
def test_int_name_format(self, klass):
    index = Index(['a', 'b', 'c'], name=0)
    result = klass(list(range(3)), index=index)
    assert '0' in repr(result)