def test_read_json_table_convert_axes_raises(self):
    df = DataFrame([[1, 2], [3, 4]], index=[1.0, 2.0], columns=['1.', '2.'])
    dfjson = df.to_json(orient='table')
    msg = "cannot pass both convert_axes and orient='table'"
    with pytest.raises(ValueError, match=msg):
        pd.read_json(dfjson, orient='table', convert_axes=True)