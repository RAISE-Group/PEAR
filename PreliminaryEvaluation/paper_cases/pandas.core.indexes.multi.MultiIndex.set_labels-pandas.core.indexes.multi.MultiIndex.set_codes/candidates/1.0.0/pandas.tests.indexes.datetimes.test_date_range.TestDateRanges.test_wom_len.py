@pytest.mark.parametrize('periods', (1, 2))
def test_wom_len(self, periods):
    res = date_range(start='20110101', periods=periods, freq='WOM-1MON')
    assert len(res) == periods