def test_head_tail(self):
    o = self._construct(shape=10)
    for index in [tm.makeFloatIndex, tm.makeIntIndex, tm.makeStringIndex, tm.makeUnicodeIndex, tm.makeDateIndex, tm.makePeriodIndex]:
        axis = o._get_axis_name(0)
        setattr(o, axis, index(len(getattr(o, axis))))
        o.head()
        self._compare(o.head(), o.iloc[:5])
        self._compare(o.tail(), o.iloc[-5:])
        self._compare(o.head(0), o.iloc[0:0])
        self._compare(o.tail(0), o.iloc[0:0])
        self._compare(o.head(len(o) + 1), o)
        self._compare(o.tail(len(o) + 1), o)
        self._compare(o.head(-3), o.head(7))
        self._compare(o.tail(-3), o.tail(7))