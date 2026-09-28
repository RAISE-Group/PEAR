@pytest.mark.parametrize('value', ['3000/12/11 00:00:00'])
@pytest.mark.parametrize('infer', [True, False])
@pytest.mark.parametrize('format', [None, 'H%:M%:S%'])
def test_datetime_outofbounds_scalar(self, value, format, infer):
    res = pd.to_datetime(value, errors='ignore', format=format, infer_datetime_format=infer)
    assert res == value
    res = pd.to_datetime(value, errors='coerce', format=format, infer_datetime_format=infer)
    assert res is pd.NaT
    if format is not None:
        with pytest.raises(ValueError):
            pd.to_datetime(value, errors='raise', format=format, infer_datetime_format=infer)
    else:
        with pytest.raises(OutOfBoundsDatetime):
            pd.to_datetime(value, errors='raise', format=format, infer_datetime_format=infer)