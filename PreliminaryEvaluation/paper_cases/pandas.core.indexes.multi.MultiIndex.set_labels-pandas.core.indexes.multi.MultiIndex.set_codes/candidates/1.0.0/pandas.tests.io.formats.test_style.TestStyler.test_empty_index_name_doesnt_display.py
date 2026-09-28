def test_empty_index_name_doesnt_display(self):
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
    result = df.style._translate()
    expected = [[{'class': 'blank level0', 'type': 'th', 'value': '', 'is_visible': True, 'display_value': ''}, {'class': 'col_heading level0 col0', 'display_value': 'A', 'type': 'th', 'value': 'A', 'is_visible': True}, {'class': 'col_heading level0 col1', 'display_value': 'B', 'type': 'th', 'value': 'B', 'is_visible': True}, {'class': 'col_heading level0 col2', 'display_value': 'C', 'type': 'th', 'value': 'C', 'is_visible': True}]]
    assert result['head'] == expected