@pytest.mark.parametrize('value', ['a', '00:01:99'])
@pytest.mark.parametrize('infer', [True, False])
@pytest.mark.parametrize('format', [None, 'H%:M%:S%'])
def test_datetime_invalid_scalar(self, value, format, infer):
    res = pd.to_datetime(value, errors='ignore', format=format, infer_datetime_format=infer)
    assert res == value
    res = pd.to_datetime(value, errors='coerce', format=format, infer_datetime_format=infer)
    assert res is pd.NaT
    with pytest.raises(ValueError):
        pd.to_datetime(value, errors='raise', format=format, infer_datetime_format=infer)