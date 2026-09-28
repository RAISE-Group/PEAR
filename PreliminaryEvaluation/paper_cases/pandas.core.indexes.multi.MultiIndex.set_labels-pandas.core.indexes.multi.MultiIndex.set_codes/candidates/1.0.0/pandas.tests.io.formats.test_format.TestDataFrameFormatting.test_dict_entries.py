def test_dict_entries(self):
    df = DataFrame({'A': [{'a': 1, 'b': 2}]})
    val = df.to_string()
    assert "'a': 1" in val
    assert "'b': 2" in val