@pytest.mark.parametrize('method', ['strip', 'rstrip', 'lstrip'])
def test_str_attribute(self, method):
    index = Index([' jack', 'jill ', ' jesse ', 'frank'])
    expected = Index([getattr(str, method)(x) for x in index.values])
    result = getattr(index.str, method)()
    tm.assert_index_equal(result, expected)