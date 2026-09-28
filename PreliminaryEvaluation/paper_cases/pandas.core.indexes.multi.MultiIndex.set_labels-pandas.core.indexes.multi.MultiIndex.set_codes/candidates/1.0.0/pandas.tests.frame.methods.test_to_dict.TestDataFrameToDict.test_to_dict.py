@pytest.mark.parametrize('mapping', [dict, defaultdict(list), OrderedDict])
def test_to_dict(self, mapping):
    test_data = {'A': {'1': 1, '2': 2}, 'B': {'1': '1', '2': '2', '3': '3'}}
    recons_data = DataFrame(test_data).to_dict(into=mapping)
    for k, v in test_data.items():
        for k2, v2 in v.items():
            assert v2 == recons_data[k][k2]
    recons_data = DataFrame(test_data).to_dict('l', mapping)
    for k, v in test_data.items():
        for k2, v2 in v.items():
            assert v2 == recons_data[k][int(k2) - 1]
    recons_data = DataFrame(test_data).to_dict('s', mapping)
    for k, v in test_data.items():
        for k2, v2 in v.items():
            assert v2 == recons_data[k][k2]
    recons_data = DataFrame(test_data).to_dict('sp', mapping)
    expected_split = {'columns': ['A', 'B'], 'index': ['1', '2', '3'], 'data': [[1.0, '1'], [2.0, '2'], [np.nan, '3']]}
    tm.assert_dict_equal(recons_data, expected_split)
    recons_data = DataFrame(test_data).to_dict('r', mapping)
    expected_records = [{'A': 1.0, 'B': '1'}, {'A': 2.0, 'B': '2'}, {'A': np.nan, 'B': '3'}]
    assert isinstance(recons_data, list)
    assert len(recons_data) == 3
    for l, r in zip(recons_data, expected_records):
        tm.assert_dict_equal(l, r)
    recons_data = DataFrame(test_data).to_dict('i')
    for k, v in test_data.items():
        for k2, v2 in v.items():
            assert v2 == recons_data[k2][k]
    df = DataFrame(test_data)
    df['duped'] = df[df.columns[0]]
    recons_data = df.to_dict('i')
    comp_data = test_data.copy()
    comp_data['duped'] = comp_data[df.columns[0]]
    for k, v in comp_data.items():
        for k2, v2 in v.items():
            assert v2 == recons_data[k2][k]