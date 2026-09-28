@pytest.mark.parametrize('htable, tm_dtype', [(ht.PyObjectHashTable, 'String'), (ht.StringHashTable, 'String'), (ht.Float64HashTable, 'Float'), (ht.Int64HashTable, 'Int'), (ht.UInt64HashTable, 'UInt')])
def test_hashtable_factorize(self, htable, tm_dtype, writable):
    maker = getattr(tm, 'make' + tm_dtype + 'Index')
    s = Series(maker(1000))
    if htable == ht.Float64HashTable:
        s.loc[500] = np.nan
    elif htable == ht.PyObjectHashTable:
        s.loc[500:502] = [np.nan, None, pd.NaT]
    s_duplicated = s.sample(frac=3, replace=True).reset_index(drop=True)
    s_duplicated.values.setflags(write=writable)
    na_mask = s_duplicated.isna().values
    result_unique, result_inverse = htable().factorize(s_duplicated.values)
    expected_unique = s_duplicated.dropna().drop_duplicates().values
    tm.assert_numpy_array_equal(result_unique, expected_unique)
    result_reconstruct = result_unique[result_inverse[~na_mask]]
    expected_reconstruct = s_duplicated.dropna().values
    tm.assert_numpy_array_equal(result_reconstruct, expected_reconstruct)