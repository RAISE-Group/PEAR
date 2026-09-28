def test_compare_different_lengths(self):
    c1 = Categorical([], categories=['a', 'b'])
    c2 = Categorical([], categories=['a'])
    msg = 'Categories are different lengths'
    with pytest.raises(TypeError, match=msg):
        c1 == c2