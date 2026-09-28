@pytest.mark.xfail(reason="see GH#21311: Index doesn't enforce dtype argument")
def test_constructor_cast(self):
    msg = 'could not convert string to float'
    with pytest.raises(ValueError, match=msg):
        Index(['a', 'b', 'c'], dtype=float)