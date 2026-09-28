@pytest.mark.parametrize('values', [['a'], ['00:01:99'], ['a', 'b', '99:00:00']])
@pytest.mark.parametrize('infer', [True, False])
@pytest.mark.parametrize('format', [None, 'H%:M%:S%'])
def test_datetime_invalid_index(self, values, format, infer):
    res = pd.to_datetime(values, errors='ignore', format=format, infer_datetime_format=infer)
    tm.assert_index_equal(res, pd.Index(values))
    res = pd.to_datetime(values, errors='coerce', format=format, infer_datetime_format=infer)
    tm.assert_index_equal(res, pd.DatetimeIndex([pd.NaT] * len(values)))
    with pytest.raises(ValueError):
        pd.to_datetime(values, errors='raise', format=format, infer_datetime_format=infer)