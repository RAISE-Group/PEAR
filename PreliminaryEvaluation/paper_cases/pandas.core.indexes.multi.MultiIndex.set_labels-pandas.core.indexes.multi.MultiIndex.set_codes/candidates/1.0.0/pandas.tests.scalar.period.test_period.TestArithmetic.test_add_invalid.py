def test_add_invalid(self):
    per1 = Period(freq='D', year=2008, month=1, day=1)
    per2 = Period(freq='D', year=2008, month=1, day=2)
    msg = 'unsupported operand type\\(s\\)'
    with pytest.raises(TypeError, match=msg):
        per1 + 'str'
    with pytest.raises(TypeError, match=msg):
        'str' + per1
    with pytest.raises(TypeError, match=msg):
        per1 + per2