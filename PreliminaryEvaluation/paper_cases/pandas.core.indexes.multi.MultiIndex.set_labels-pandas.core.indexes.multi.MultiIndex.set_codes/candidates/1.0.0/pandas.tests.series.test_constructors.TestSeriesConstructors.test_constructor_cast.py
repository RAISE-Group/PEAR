def test_constructor_cast(self):
    msg = 'could not convert string to float'
    with pytest.raises(ValueError, match=msg):
        Series(['a', 'b', 'c'], dtype=float)