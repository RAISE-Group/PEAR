def test_is_string_array(self):
    assert lib.is_string_array(np.array(['foo', 'bar']))
    assert not lib.is_string_array(np.array(['foo', 'bar', pd.NA], dtype=object), skipna=False)
    assert lib.is_string_array(np.array(['foo', 'bar', pd.NA], dtype=object), skipna=True)
    assert not lib.is_string_array(np.array(['foo', 'bar', np.nan], dtype=object), skipna=True)
    assert not lib.is_string_array(np.array([1, 2]))