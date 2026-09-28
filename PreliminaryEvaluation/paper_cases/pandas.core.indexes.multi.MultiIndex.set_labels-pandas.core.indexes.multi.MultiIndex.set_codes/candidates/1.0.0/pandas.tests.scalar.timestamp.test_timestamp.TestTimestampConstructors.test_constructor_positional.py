def test_constructor_positional(self):
    with pytest.raises(TypeError):
        Timestamp(2000, 1)
    with pytest.raises(ValueError):
        Timestamp(2000, 0, 1)
    with pytest.raises(ValueError):
        Timestamp(2000, 13, 1)
    with pytest.raises(ValueError):
        Timestamp(2000, 1, 0)
    with pytest.raises(ValueError):
        Timestamp(2000, 1, 32)
    assert repr(Timestamp(2015, 11, 12)) == repr(Timestamp('20151112'))
    assert repr(Timestamp(2015, 11, 12, 1, 2, 3, 999999)) == repr(Timestamp('2015-11-12 01:02:03.999999'))