def test_one_level_deep_flattens(self):
    data = dict(flat1=1, dict1=dict(c=1, d=2))
    result = nested_to_record(data)
    expected = {'dict1.c': 1, 'dict1.d': 2, 'flat1': 1}
    assert result == expected