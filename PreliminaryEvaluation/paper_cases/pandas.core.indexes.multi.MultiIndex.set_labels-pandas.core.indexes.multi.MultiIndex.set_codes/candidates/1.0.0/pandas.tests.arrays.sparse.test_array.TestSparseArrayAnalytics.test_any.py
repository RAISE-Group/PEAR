@pytest.mark.parametrize('data,pos,neg', [([False, True, False], True, False), ([0, 2, 0], 2, 0), ([0.0, 2.0, 0.0], 2.0, 0.0)])
def test_any(self, data, pos, neg):
    out = SparseArray(data).any()
    assert out
    out = SparseArray(data, fill_value=pos).any()
    assert out
    data[1] = neg
    out = SparseArray(data).any()
    assert not out
    out = SparseArray(data, fill_value=pos).any()
    assert not out