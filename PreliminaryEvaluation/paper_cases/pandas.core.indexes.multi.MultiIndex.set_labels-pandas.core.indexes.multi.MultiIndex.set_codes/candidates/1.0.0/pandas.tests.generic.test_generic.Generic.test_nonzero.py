def test_nonzero(self):
    obj = self._construct(shape=4)
    msg = f'The truth value of a {self._typ.__name__} is ambiguous'
    with pytest.raises(ValueError, match=msg):
        bool(obj == 0)
    with pytest.raises(ValueError, match=msg):
        bool(obj == 1)
    with pytest.raises(ValueError, match=msg):
        bool(obj)
    obj = self._construct(shape=4, value=1)
    with pytest.raises(ValueError, match=msg):
        bool(obj == 0)
    with pytest.raises(ValueError, match=msg):
        bool(obj == 1)
    with pytest.raises(ValueError, match=msg):
        bool(obj)
    obj = self._construct(shape=4, value=np.nan)
    with pytest.raises(ValueError, match=msg):
        bool(obj == 0)
    with pytest.raises(ValueError, match=msg):
        bool(obj == 1)
    with pytest.raises(ValueError, match=msg):
        bool(obj)
    obj = self._construct(shape=0)
    with pytest.raises(ValueError, match=msg):
        bool(obj)
    obj1 = self._construct(shape=4, value=1)
    obj2 = self._construct(shape=4, value=1)
    with pytest.raises(ValueError, match=msg):
        if obj1:
            pass
    with pytest.raises(ValueError, match=msg):
        obj1 and obj2
    with pytest.raises(ValueError, match=msg):
        obj1 or obj2
    with pytest.raises(ValueError, match=msg):
        not obj1