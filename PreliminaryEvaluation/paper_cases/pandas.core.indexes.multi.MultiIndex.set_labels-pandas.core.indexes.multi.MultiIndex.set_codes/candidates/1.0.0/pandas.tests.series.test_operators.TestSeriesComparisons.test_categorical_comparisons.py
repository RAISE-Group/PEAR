def test_categorical_comparisons(self):
    a = Series(list('abc'), dtype='category')
    b = Series(list('abc'), dtype='object')
    c = Series(['a', 'b', 'cc'], dtype='object')
    d = Series(list('acb'), dtype='object')
    e = Categorical(list('abc'))
    f = Categorical(list('acb'))
    assert not (a == 'a').all()
    assert ((a != 'a') == ~(a == 'a')).all()
    assert not ('a' == a).all()
    assert (a == 'a')[0]
    assert ('a' == a)[0]
    assert not ('a' != a)[0]
    assert (a == a).all()
    assert not (a != a).all()
    assert (a == list(a)).all()
    assert (a == b).all()
    assert (b == a).all()
    assert (~(a == b) == (a != b)).all()
    assert (~(b == a) == (b != a)).all()
    assert not (a == c).all()
    assert not (c == a).all()
    assert not (a == d).all()
    assert not (d == a).all()
    assert (a == e).all()
    assert (e == a).all()
    assert not (a == f).all()
    assert not (f == a).all()
    assert (~(a == e) == (a != e)).all()
    assert (~(e == a) == (e != a)).all()
    assert (~(a == f) == (a != f)).all()
    assert (~(f == a) == (f != a)).all()
    with pytest.raises(TypeError):
        a < b
    with pytest.raises(TypeError):
        b < a
    with pytest.raises(TypeError):
        a > b
    with pytest.raises(TypeError):
        b > a