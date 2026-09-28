def test_rename(self):
    idx = list('ABCD')
    args = [str.lower, {x: x.lower() for x in idx}, Series({x: x.lower() for x in idx})]
    for axis in self._axes():
        kwargs = {axis: idx}
        obj = self._construct(4, **kwargs)
        for arg in args:
            result = obj.rename(**{axis: arg})
            expected = obj.copy()
            setattr(expected, axis, list('abcd'))
            self._compare(result, expected)