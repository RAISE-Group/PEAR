def test_str_vs_repr(self, ordered_fixture):
    c1 = CategoricalDtype(['a', 'b'], ordered=ordered_fixture)
    assert str(c1) == 'category'
    pat = 'CategoricalDtype\\(categories=\\[.*\\], ordered={ordered}\\)'
    assert re.match(pat.format(ordered=ordered_fixture), repr(c1))