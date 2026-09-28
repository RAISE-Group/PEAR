def test_mi_sparse(self):
    df = pd.DataFrame({'A': [1, 2]}, index=pd.MultiIndex.from_arrays([['a', 'a'], [0, 1]]))
    result = df.style._translate()
    body_0 = result['body'][0][0]
    expected_0 = {'value': 'a', 'display_value': 'a', 'is_visible': True, 'type': 'th', 'attributes': ['rowspan=2'], 'class': 'row_heading level0 row0', 'id': 'level0_row0'}
    tm.assert_dict_equal(body_0, expected_0)
    body_1 = result['body'][0][1]
    expected_1 = {'value': 0, 'display_value': 0, 'is_visible': True, 'type': 'th', 'class': 'row_heading level1 row0', 'id': 'level1_row0'}
    tm.assert_dict_equal(body_1, expected_1)
    body_10 = result['body'][1][0]
    expected_10 = {'value': 'a', 'display_value': 'a', 'is_visible': False, 'type': 'th', 'class': 'row_heading level0 row1', 'id': 'level0_row1'}
    tm.assert_dict_equal(body_10, expected_10)
    head = result['head'][0]
    expected = [{'type': 'th', 'class': 'blank', 'value': '', 'is_visible': True, 'display_value': ''}, {'type': 'th', 'class': 'blank level0', 'value': '', 'is_visible': True, 'display_value': ''}, {'type': 'th', 'class': 'col_heading level0 col0', 'value': 'A', 'is_visible': True, 'display_value': 'A'}]
    assert head == expected