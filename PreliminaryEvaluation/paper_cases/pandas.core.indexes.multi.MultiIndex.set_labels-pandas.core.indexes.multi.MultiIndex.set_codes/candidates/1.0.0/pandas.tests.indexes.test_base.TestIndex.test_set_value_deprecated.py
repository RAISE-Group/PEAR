def test_set_value_deprecated(self):
    idx = self.create_index()
    arr = np.array([1, 2, 3])
    with tm.assert_produces_warning(FutureWarning):
        idx.set_value(arr, idx[1], 80)
    assert arr[1] == 80