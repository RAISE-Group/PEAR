def test_to_dict_numeric_names(self):
    df = DataFrame({str(i): [i] for i in range(5)})
    result = set(df.to_dict('records')[0].keys())
    expected = set(df.columns)
    assert result == expected