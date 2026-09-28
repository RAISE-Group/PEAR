def test_get_value(self):
    dti = pd.date_range('2016-01-01', periods=3)
    arr = np.arange(6, 8)
    key = dti[1]
    result = dti.get_value(arr, key)
    assert result == 7
    result = dti.get_value(arr, key.to_pydatetime())
    assert result == 7
    result = dti.get_value(arr, key.to_datetime64())
    assert result == 7