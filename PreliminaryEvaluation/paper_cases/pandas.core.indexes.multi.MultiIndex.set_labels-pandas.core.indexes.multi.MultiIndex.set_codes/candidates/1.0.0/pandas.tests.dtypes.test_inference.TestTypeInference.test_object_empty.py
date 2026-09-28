@pytest.mark.parametrize('dtype, missing, skipna, expected', [(float, np.nan, False, 'floating'), (float, np.nan, True, 'floating'), (object, np.nan, False, 'floating'), (object, np.nan, True, 'empty'), (object, None, False, 'mixed'), (object, None, True, 'empty')])
@pytest.mark.parametrize('box', [pd.Series, np.array])
def test_object_empty(self, box, missing, dtype, skipna, expected):
    arr = box([missing, missing], dtype=dtype)
    result = lib.infer_dtype(arr, skipna=skipna)
    assert result == expected