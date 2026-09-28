@pytest.mark.parametrize('op', [operator.add, ops.radd, operator.sub, ops.rsub])
def test_objarr_add_invalid(self, op, box_with_array):
    box = box_with_array
    obj_ser = tm.makeObjectSeries()
    obj_ser.name = 'objects'
    obj_ser = tm.box_expected(obj_ser, box)
    with pytest.raises(Exception):
        op(obj_ser, 1)
    with pytest.raises(Exception):
        op(obj_ser, np.array(1, dtype=np.int64))