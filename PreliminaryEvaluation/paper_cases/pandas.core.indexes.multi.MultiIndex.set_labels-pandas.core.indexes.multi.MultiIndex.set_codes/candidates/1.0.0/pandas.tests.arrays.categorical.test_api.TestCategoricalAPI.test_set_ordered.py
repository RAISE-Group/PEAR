def test_set_ordered(self):
    cat = Categorical(['a', 'b', 'c', 'a'], ordered=True)
    cat2 = cat.as_unordered()
    assert not cat2.ordered
    cat2 = cat.as_ordered()
    assert cat2.ordered
    cat2.as_unordered(inplace=True)
    assert not cat2.ordered
    cat2.as_ordered(inplace=True)
    assert cat2.ordered
    assert cat2.set_ordered(True).ordered
    assert not cat2.set_ordered(False).ordered
    cat2.set_ordered(True, inplace=True)
    assert cat2.ordered
    cat2.set_ordered(False, inplace=True)
    assert not cat2.ordered
    msg = "can't set attribute"
    with pytest.raises(AttributeError, match=msg):
        cat.ordered = True
    with pytest.raises(AttributeError, match=msg):
        cat.ordered = False