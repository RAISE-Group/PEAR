@pytest.mark.parametrize('data,pos,neg', [([True, True, True], True, False), ([1, 2, 1], 1, 0), ([1.0, 2.0, 1.0], 1.0, 0.0)])
def test_all(self, data, pos, neg):
    out = SparseArray(data).all()
    assert out
    out = SparseArray(data, fill_value=pos).all()
    assert out
    data[1] = neg
    out = SparseArray(data).all()
    assert not out
    out = SparseArray(data, fill_value=pos).all()
    assert not out