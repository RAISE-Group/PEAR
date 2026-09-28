@pytest.mark.parametrize('index', [None, [1, 2], [1.0, 2.0], ['a', 'b'], ['1', '2'], ['1.', '2.']])
@pytest.mark.parametrize('columns', [['a', 'b'], ['1', '2'], ['1.', '2.']])
def test_from_json_to_json_table_index_and_columns(self, index, columns):
    expected = DataFrame([[1, 2], [3, 4]], index=index, columns=columns)
    dfjson = expected.to_json(orient='table')
    result = pd.read_json(dfjson, orient='table')
    tm.assert_frame_equal(result, expected)