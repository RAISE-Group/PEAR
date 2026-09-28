def test_misspecified(self):
    with pytest.raises(ValueError, match='Month must go from 1 to 12'):
        YearBegin(month=13)