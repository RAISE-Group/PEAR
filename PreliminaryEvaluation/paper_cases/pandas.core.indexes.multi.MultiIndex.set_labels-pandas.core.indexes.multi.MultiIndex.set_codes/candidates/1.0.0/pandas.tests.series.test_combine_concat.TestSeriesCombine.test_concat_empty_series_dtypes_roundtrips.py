def test_concat_empty_series_dtypes_roundtrips(self):
    dtypes = map(np.dtype, ['float64', 'int8', 'uint8', 'bool', 'm8[ns]', 'M8[ns]'])
    for dtype in dtypes:
        assert pd.concat([Series(dtype=dtype)]).dtype == dtype
        assert pd.concat([Series(dtype=dtype), Series(dtype=dtype)]).dtype == dtype

    def int_result_type(dtype, dtype2):
        typs = {dtype.kind, dtype2.kind}
        if not len(typs - {'i', 'u', 'b'}) and (dtype.kind == 'i' or dtype2.kind == 'i'):
            return 'i'
        elif not len(typs - {'u', 'b'}) and (dtype.kind == 'u' or dtype2.kind == 'u'):
            return 'u'
        return None

    def float_result_type(dtype, dtype2):
        typs = {dtype.kind, dtype2.kind}
        if not len(typs - {'f', 'i', 'u'}) and (dtype.kind == 'f' or dtype2.kind == 'f'):
            return 'f'
        return None

    def get_result_type(dtype, dtype2):
        result = float_result_type(dtype, dtype2)
        if result is not None:
            return result
        result = int_result_type(dtype, dtype2)
        if result is not None:
            return result
        return 'O'
    for dtype in dtypes:
        for dtype2 in dtypes:
            if dtype == dtype2:
                continue
            expected = get_result_type(dtype, dtype2)
            result = pd.concat([Series(dtype=dtype), Series(dtype=dtype2)]).dtype
            assert result.kind == expected