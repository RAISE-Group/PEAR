@pytest.mark.parametrize('hashtable', [ht.PyObjectHashTable, ht.StringHashTable, ht.Float64HashTable, ht.Int64HashTable, ht.UInt64HashTable])
def test_hashtable_large_sizehint(self, hashtable):
    size_hint = np.iinfo(np.uint32).max + 1
    tbl = hashtable(size_hint=size_hint)