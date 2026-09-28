def test_misspecified(self):
    with pytest.raises(ValueError, match='Month must go from 1 to 12'):
        YearEnd(month=13)