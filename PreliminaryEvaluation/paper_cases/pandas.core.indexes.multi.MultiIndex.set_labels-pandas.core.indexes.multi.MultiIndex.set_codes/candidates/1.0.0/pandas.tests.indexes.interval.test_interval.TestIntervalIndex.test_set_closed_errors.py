@pytest.mark.parametrize('bad_closed', ['foo', 10, 'LEFT', True, False])
def test_set_closed_errors(self, bad_closed):
    index = interval_range(0, 5)
    msg = "invalid option for 'closed': {closed}".format(closed=bad_closed)
    with pytest.raises(ValueError, match=msg):
        index.set_closed(bad_closed)