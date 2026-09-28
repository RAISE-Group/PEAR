def test_join_unconsolidated(self):
    a = DataFrame(randn(30, 2), columns=['a', 'b'])
    c = Series(randn(30))
    a['c'] = c
    d = DataFrame(randn(30, 1), columns=['q'])
    a.join(d)
    d.join(a)