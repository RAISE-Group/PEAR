@pytest.mark.parametrize('setter', ['loc', None])
def test_setitem_mask_broadcast(self, data, setter):
    ser = pd.Series(data)
    mask = np.zeros(len(data), dtype=bool)
    mask[:2] = True
    if setter:
        target = getattr(ser, setter)
    else:
        target = ser
    operator.setitem(target, mask, data[10])
    assert ser[0] == data[10]
    assert ser[1] == data[10]