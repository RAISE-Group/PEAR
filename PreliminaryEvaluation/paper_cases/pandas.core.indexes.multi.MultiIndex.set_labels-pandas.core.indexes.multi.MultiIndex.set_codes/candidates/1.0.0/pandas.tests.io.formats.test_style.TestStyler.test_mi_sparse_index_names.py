def test_mi_sparse_index_names(self):
    df = pd.DataFrame({'A': [1, 2]}, index=pd.MultiIndex.from_arrays([['a', 'a'], [0, 1]], names=['idx_level_0', 'idx_level_1']))
    result = df.style._translate()
    head = result['head'][1]
    expected = [{'class': 'index_name level0', 'value': 'idx_level_0', 'type': 'th'}, {'class': 'index_name level1', 'value': 'idx_level_1', 'type': 'th'}, {'class': 'blank', 'value': '', 'type': 'th'}]
    assert head == expected