def test_get_item(self):
    assert np.isnan(self.arr[1])
    assert self.arr[2] == 1
    assert self.arr[7] == 5
    assert self.zarr[0] == 0
    assert self.zarr[2] == 1
    assert self.zarr[7] == 5
    errmsg = re.compile('bounds')
    with pytest.raises(IndexError, match=errmsg):
        self.arr[11]
    with pytest.raises(IndexError, match=errmsg):
        self.arr[-11]
    assert self.arr[-1] == self.arr[len(self.arr) - 1]