def test_index_name(self):
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
    result = df.set_index('A').style._translate()
    expected = [[{'class': 'blank level0', 'type': 'th', 'value': '', 'display_value': '', 'is_visible': True}, {'class': 'col_heading level0 col0', 'type': 'th', 'value': 'B', 'display_value': 'B', 'is_visible': True}, {'class': 'col_heading level0 col1', 'type': 'th', 'value': 'C', 'display_value': 'C', 'is_visible': True}], [{'class': 'index_name level0', 'type': 'th', 'value': 'A'}, {'class': 'blank', 'type': 'th', 'value': ''}, {'class': 'blank', 'type': 'th', 'value': ''}]]
    assert result['head'] == expected