@pytest.mark.parametrize('method', ['pad', 'backfill'])
def test_fillna_preserves_tz(self, method):
    dti = pd.date_range('2000-01-01', periods=5, freq='D', tz='US/Central')
    arr = DatetimeArray(dti, copy=True)
    arr[2] = pd.NaT
    fill_val = dti[1] if method == 'pad' else dti[3]
    expected = DatetimeArray._from_sequence([dti[0], dti[1], fill_val, dti[3], dti[4]], freq=None, tz='US/Central')
    result = arr.fillna(method=method)
    tm.assert_extension_array_equal(result, expected)
    assert arr[2] is pd.NaT
    assert dti[2] == pd.Timestamp('2000-01-03', tz='US/Central')