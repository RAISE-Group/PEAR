def test_add_signed_zeros(self):
    N = 4
    m = ht.Float64HashTable(N)
    m.set_item(0.0, 0)
    m.set_item(-0.0, 0)
    assert len(m) == 1