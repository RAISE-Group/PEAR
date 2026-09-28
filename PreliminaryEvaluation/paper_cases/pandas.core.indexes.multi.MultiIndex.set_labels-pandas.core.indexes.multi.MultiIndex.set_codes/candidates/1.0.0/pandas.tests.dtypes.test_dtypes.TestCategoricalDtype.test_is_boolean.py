@pytest.mark.parametrize('categories, expected', [([True, False], True), ([True, False, None], True), ([True, False, 'a', "b'"], False), ([0, 1], False)])
def test_is_boolean(self, categories, expected):
    cat = Categorical(categories)
    assert cat.dtype._is_boolean is expected
    assert is_bool_dtype(cat) is expected
    assert is_bool_dtype(cat.dtype) is expected