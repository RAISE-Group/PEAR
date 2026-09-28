@pytest.mark.parametrize('lbox', boxes, ids=ids)
@pytest.mark.parametrize('rbox', boxes, ids=ids)
def test_add_timestamp_raises(self, rbox, lbox):
    ts = Timestamp('2017')
    per = Period('2017', freq='M')
    msg = 'cannot add|unsupported operand|can only operate on a|incompatible type|ufunc add cannot use operands'
    with pytest.raises(TypeError, match=msg):
        lbox(ts) + rbox(per)
    with pytest.raises(TypeError, match=msg):
        lbox(per) + rbox(ts)
    with pytest.raises(TypeError, match=msg):
        lbox(per) + rbox(per)