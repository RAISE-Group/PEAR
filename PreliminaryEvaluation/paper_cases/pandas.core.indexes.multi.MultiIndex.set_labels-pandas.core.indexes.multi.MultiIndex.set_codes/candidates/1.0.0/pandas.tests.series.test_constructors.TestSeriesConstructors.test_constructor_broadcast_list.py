def test_constructor_broadcast_list(self):
    msg = 'Length of passed values is 1, index implies 3'
    with pytest.raises(ValueError, match=msg):
        Series(['foo'], index=['a', 'b', 'c'])