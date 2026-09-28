def test_take_empty(self, allow_fill):
    cat = pd.Categorical([], categories=['a', 'b'])
    if allow_fill:
        msg = 'indices are out-of-bounds'
    else:
        msg = 'cannot do a non-empty take from an empty axes'
    with pytest.raises(IndexError, match=msg):
        cat.take([0], allow_fill=allow_fill)