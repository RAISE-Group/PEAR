@pytest.mark.parametrize('td', [Timedelta(hours=3), np.timedelta64(3, 'h'), timedelta(hours=3)])
def test_radd_tdscalar(self, td):
    ts = Timestamp.now()
    assert td + ts == ts + td