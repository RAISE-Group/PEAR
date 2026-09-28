def test_mixin(self):

    class T(NoNewAttributesMixin):
        pass
    t = T()
    assert not hasattr(t, '__frozen')
    t.a = 'test'
    assert t.a == 'test'
    t._freeze()
    assert '__frozen' in dir(t)
    assert getattr(t, '__frozen')
    with pytest.raises(AttributeError):
        t.b = 'test'
    assert not hasattr(t, 'b')