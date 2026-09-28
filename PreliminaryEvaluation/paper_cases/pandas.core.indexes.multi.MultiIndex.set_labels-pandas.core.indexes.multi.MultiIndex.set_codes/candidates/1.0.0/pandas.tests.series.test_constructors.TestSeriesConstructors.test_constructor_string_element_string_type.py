@pytest.mark.parametrize('item', ['entry', 'ѐ', 13])
def test_constructor_string_element_string_type(self, item):
    result = pd.Series(item, index=[1], dtype=str)
    assert result.iloc[0] == str(item)