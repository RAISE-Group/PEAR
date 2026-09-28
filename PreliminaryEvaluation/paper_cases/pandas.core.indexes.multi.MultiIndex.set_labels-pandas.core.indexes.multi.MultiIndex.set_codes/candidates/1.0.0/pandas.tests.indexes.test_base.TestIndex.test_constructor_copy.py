def test_constructor_copy(self, index):
    arr = np.array(index)
    new_index = Index(arr, copy=True, name='name')
    assert isinstance(new_index, Index)
    assert new_index.name == 'name'
    tm.assert_numpy_array_equal(arr, new_index.values)
    arr[0] = 'SOMEBIGLONGSTRING'
    assert new_index[0] != 'SOMEBIGLONGSTRING'