def test_empty(self):
    dt = PeriodDtype()
    with pytest.raises(AttributeError):
        str(dt)