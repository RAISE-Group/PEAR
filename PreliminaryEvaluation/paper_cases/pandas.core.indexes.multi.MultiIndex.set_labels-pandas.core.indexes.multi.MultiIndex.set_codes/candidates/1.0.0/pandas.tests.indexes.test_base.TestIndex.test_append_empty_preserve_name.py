@pytest.mark.parametrize('name,expected', [('foo', 'foo'), ('bar', None)])
def test_append_empty_preserve_name(self, name, expected):
    left = Index([], name='foo')
    right = Index([1, 2, 3], name=name)
    result = left.append(right)
    assert result.name == expected