@pytest.mark.parametrize('is_copy', [True, False])
def test_depr_take_kwarg_is_copy(self, is_copy):
    df = DataFrame({'A': [1, 2, 3]})
    msg = "is_copy is deprecated and will be removed in a future version. 'take' always returns a copy, so there is no need to specify this."
    with tm.assert_produces_warning(FutureWarning) as w:
        df.take([0, 1], is_copy=is_copy)
    assert w[0].message.args[0] == msg
    s = Series([1, 2, 3])
    with tm.assert_produces_warning(FutureWarning):
        s.take([0, 1], is_copy=is_copy)