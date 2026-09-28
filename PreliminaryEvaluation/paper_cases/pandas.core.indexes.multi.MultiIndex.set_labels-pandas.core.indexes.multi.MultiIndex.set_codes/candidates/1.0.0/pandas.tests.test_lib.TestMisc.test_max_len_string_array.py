def test_max_len_string_array(self):
    arr = a = np.array(['foo', 'b', np.nan], dtype='object')
    assert libwriters.max_len_string_array(arr) == 3
    arr = a.astype('U').astype(object)
    assert libwriters.max_len_string_array(arr) == 3
    arr = a.astype('S').astype(object)
    assert libwriters.max_len_string_array(arr) == 3
    with pytest.raises(TypeError):
        libwriters.max_len_string_array(arr.astype('U'))