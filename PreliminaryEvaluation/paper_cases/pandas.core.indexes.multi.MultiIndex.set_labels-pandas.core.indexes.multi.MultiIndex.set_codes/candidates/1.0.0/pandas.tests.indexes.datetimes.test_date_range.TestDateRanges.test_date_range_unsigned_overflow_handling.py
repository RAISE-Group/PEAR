def test_date_range_unsigned_overflow_handling(self):
    dti = date_range(start='1677-09-22', end='2262-04-11', freq='D')
    dti2 = date_range(start=dti[0], periods=len(dti), freq='D')
    assert dti2.equals(dti)
    dti3 = date_range(end=dti[-1], periods=len(dti), freq='D')
    assert dti3.equals(dti)