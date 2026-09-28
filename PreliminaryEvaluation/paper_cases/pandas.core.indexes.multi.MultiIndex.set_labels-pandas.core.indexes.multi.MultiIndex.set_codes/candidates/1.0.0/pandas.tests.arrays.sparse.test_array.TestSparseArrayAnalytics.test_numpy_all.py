@pytest.mark.parametrize('data,pos,neg', [([True, True, True], True, False), ([1, 2, 1], 1, 0), ([1.0, 2.0, 1.0], 1.0, 0.0)])
@td.skip_if_np_lt('1.15')
def test_numpy_all(self, data, pos, neg):
    out = np.all(SparseArray(data))
    assert out
    out = np.all(SparseArray(data, fill_value=pos))
    assert out
    data[1] = neg
    out = np.all(SparseArray(data))
    assert not out
    out = np.all(SparseArray(data, fill_value=pos))
    assert not out
    msg = "the 'out' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.all(SparseArray(data), out=np.array([]))