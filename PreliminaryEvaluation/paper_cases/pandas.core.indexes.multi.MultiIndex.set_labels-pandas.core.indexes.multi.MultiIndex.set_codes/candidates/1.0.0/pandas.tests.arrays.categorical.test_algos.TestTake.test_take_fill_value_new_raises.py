def test_take_fill_value_new_raises(self):
    cat = pd.Categorical(['a', 'b', 'c'])
    xpr = "'fill_value' \\('d'\\) is not in this Categorical's categories."
    with pytest.raises(TypeError, match=xpr):
        cat.take([0, 1, -1], fill_value='d', allow_fill=True)