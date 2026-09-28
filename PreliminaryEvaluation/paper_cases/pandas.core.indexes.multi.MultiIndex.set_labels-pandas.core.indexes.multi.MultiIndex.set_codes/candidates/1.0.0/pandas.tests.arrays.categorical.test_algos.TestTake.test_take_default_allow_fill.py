def test_take_default_allow_fill(self):
    cat = pd.Categorical(['a', 'b'])
    with tm.assert_produces_warning(None):
        result = cat.take([0, -1])
    assert result.equals(cat)