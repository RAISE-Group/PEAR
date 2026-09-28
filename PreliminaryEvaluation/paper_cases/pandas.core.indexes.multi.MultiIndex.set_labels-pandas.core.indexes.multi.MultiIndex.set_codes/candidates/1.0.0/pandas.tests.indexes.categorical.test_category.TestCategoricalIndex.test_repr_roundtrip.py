def test_repr_roundtrip(self):
    ci = CategoricalIndex(['a', 'b'], categories=['a', 'b'], ordered=True)
    str(ci)
    tm.assert_index_equal(eval(repr(ci)), ci, exact=True)
    str(ci)
    ci = CategoricalIndex(np.random.randint(0, 5, size=100))
    str(ci)