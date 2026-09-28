@pytest.mark.parametrize('dtype', [True, {'b': int, 'c': int}])
def test_read_json_table_dtype_raises(self, dtype):
    df = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0], 'c': ['5', '6']})
    dfjson = df.to_json(orient='table')
    msg = "cannot pass both dtype and orient='table'"
    with pytest.raises(ValueError, match=msg):
        pd.read_json(dfjson, orient='table', dtype=dtype)