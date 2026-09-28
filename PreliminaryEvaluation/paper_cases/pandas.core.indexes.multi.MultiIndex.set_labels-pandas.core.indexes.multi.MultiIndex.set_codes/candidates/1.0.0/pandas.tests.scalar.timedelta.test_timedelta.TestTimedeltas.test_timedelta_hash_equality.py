def test_timedelta_hash_equality(self):
    v = Timedelta(1, 'D')
    td = timedelta(days=1)
    assert hash(v) == hash(td)
    d = {td: 2}
    assert d[v] == 2
    tds = timedelta_range('1 second', periods=20)
    assert all((hash(td) == hash(td.to_pytimedelta()) for td in tds))
    ns_td = Timedelta(1, 'ns')
    assert hash(ns_td) != hash(ns_td.to_pytimedelta())