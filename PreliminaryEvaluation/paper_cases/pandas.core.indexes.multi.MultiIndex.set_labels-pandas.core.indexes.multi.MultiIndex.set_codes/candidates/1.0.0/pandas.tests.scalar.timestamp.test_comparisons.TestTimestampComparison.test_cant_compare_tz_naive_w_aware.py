def test_cant_compare_tz_naive_w_aware(self, utc_fixture):
    a = Timestamp('3/12/2012')
    b = Timestamp('3/12/2012', tz=utc_fixture)
    with pytest.raises(TypeError):
        a == b
    with pytest.raises(TypeError):
        a != b
    with pytest.raises(TypeError):
        a < b
    with pytest.raises(TypeError):
        a <= b
    with pytest.raises(TypeError):
        a > b
    with pytest.raises(TypeError):
        a >= b
    with pytest.raises(TypeError):
        b == a
    with pytest.raises(TypeError):
        b != a
    with pytest.raises(TypeError):
        b < a
    with pytest.raises(TypeError):
        b <= a
    with pytest.raises(TypeError):
        b > a
    with pytest.raises(TypeError):
        b >= a
    assert not a == b.to_pydatetime()
    assert not a.to_pydatetime() == b