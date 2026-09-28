@pytest.mark.parametrize('htable, tm_dtype', [(ht.PyObjectHashTable, 'String'), (ht.StringHashTable, 'String'), (ht.Float64HashTable, 'Float'), (ht.Int64HashTable, 'Int'), (ht.UInt64HashTable, 'UInt')])
def test_hashtable_unique(self, htable, tm_dtype, writable):
    maker = getattr(tm, 'make' + tm_dtype + 'Index')
    s = Series(maker(1000))
    if htable == ht.Float64HashTable:
        s.loc[500] = np.nan
    elif htable == ht.PyObjectHashTable:
        s.loc[500:502] = [np.nan, None, pd.NaT]
    s_duplicated = s.sample(frac=3, replace=True).reset_index(drop=True)
    s_duplicated.values.setflags(write=writable)
    expected_unique = s_duplicated.drop_duplicates(keep='first').values
    result_unique = htable().unique(s_duplicated.values)
    tm.assert_numpy_array_equal(result_unique, expected_unique)
    result_unique, result_inverse = htable().unique(s_duplicated.values, return_inverse=True)
    tm.assert_numpy_array_equal(result_unique, expected_unique)
    reconstr = result_unique[result_inverse]
    tm.assert_numpy_array_equal(reconstr, s_duplicated.values)