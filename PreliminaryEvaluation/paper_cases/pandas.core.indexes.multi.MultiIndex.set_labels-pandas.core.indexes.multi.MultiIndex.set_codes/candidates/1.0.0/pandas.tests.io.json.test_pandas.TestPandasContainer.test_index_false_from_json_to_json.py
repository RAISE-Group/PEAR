@pytest.mark.parametrize('orient', ['split', 'table'])
@pytest.mark.parametrize('index', [True, False])
def test_index_false_from_json_to_json(self, orient, index):
    expected = DataFrame({'a': [1, 2], 'b': [3, 4]})
    dfjson = expected.to_json(orient=orient, index=index)
    result = read_json(dfjson, orient=orient)
    tm.assert_frame_equal(result, expected)