def test_string_hashtable_set_item_signature(self):
    tbl = ht.StringHashTable()
    tbl.set_item('key', 1)
    assert tbl.get_item('key') == 1
    with pytest.raises(TypeError, match="'key' has incorrect type"):
        tbl.set_item(4, 6)
    with pytest.raises(TypeError, match="'val' has incorrect type"):
        tbl.get_item(4)