@pytest.mark.parametrize('file', ['dta19_115', 'dta19_117'])
def test_categorical_ordering(self, file):
    file = getattr(self, file)
    parsed = read_stata(file)
    parsed_unordered = read_stata(file, order_categoricals=False)
    for col in parsed:
        if not is_categorical_dtype(parsed[col]):
            continue
        assert parsed[col].cat.ordered
        assert not parsed_unordered[col].cat.ordered