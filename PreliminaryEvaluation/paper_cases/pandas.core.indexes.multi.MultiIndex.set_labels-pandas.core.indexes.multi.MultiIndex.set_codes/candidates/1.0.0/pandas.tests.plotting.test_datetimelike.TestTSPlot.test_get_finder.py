def test_get_finder(self):
    import pandas.plotting._matplotlib.converter as conv
    assert conv.get_finder('B') == conv._daily_finder
    assert conv.get_finder('D') == conv._daily_finder
    assert conv.get_finder('M') == conv._monthly_finder
    assert conv.get_finder('Q') == conv._quarterly_finder
    assert conv.get_finder('A') == conv._annual_finder
    assert conv.get_finder('W') == conv._daily_finder