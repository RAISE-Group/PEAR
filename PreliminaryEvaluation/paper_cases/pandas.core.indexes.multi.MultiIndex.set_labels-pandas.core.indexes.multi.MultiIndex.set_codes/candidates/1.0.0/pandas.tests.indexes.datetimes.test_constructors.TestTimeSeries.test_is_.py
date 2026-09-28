def test_is_(self):
    dti = date_range(start='1/1/2005', end='12/1/2005', freq='M')
    assert dti.is_(dti)
    assert dti.is_(dti.view())
    assert not dti.is_(dti.copy())