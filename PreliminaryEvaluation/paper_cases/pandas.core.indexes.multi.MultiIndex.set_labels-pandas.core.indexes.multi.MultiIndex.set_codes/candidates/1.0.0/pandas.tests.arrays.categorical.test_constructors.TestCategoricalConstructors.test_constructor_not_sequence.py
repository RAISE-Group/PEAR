def test_constructor_not_sequence(self):
    msg = "^Parameter 'categories' must be list-like, was"
    with pytest.raises(TypeError, match=msg):
        Categorical(['a', 'b'], categories='a')