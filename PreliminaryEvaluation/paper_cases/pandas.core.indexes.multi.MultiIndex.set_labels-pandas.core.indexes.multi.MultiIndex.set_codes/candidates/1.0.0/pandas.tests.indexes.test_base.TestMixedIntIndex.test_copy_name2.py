def test_copy_name2(self):
    index = pd.Index([1, 2], name='MyName')
    index1 = index.copy()
    tm.assert_index_equal(index, index1)
    index2 = index.copy(name='NewName')
    tm.assert_index_equal(index, index2, check_names=False)
    assert index.name == 'MyName'
    assert index2.name == 'NewName'
    index3 = index.copy(names=['NewName'])
    tm.assert_index_equal(index, index3, check_names=False)
    assert index.name == 'MyName'
    assert index.names == ['MyName']
    assert index3.name == 'NewName'
    assert index3.names == ['NewName']