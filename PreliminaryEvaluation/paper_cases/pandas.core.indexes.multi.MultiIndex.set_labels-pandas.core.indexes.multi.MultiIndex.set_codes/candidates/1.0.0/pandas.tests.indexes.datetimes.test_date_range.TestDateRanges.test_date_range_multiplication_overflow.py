def test_date_range_multiplication_overflow(self):
    with tm.assert_produces_warning(None):
        dti = date_range(start='1677-09-22', periods=213503, freq='D')
    assert dti[0] == Timestamp('1677-09-22')
    assert len(dti) == 213503
    msg = 'Cannot generate range with'
    with pytest.raises(OutOfBoundsDatetime, match=msg):
        date_range('1969-05-04', periods=200000000, freq='30000D')