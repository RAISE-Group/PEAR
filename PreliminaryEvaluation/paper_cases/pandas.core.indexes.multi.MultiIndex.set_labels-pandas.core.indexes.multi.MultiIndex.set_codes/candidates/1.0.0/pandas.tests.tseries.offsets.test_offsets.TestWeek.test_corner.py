def test_corner(self):
    with pytest.raises(ValueError):
        Week(weekday=7)
    with pytest.raises(ValueError, match='Day must be'):
        Week(weekday=-1)