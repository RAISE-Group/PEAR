def test_anchor_week_end_time(self):

    def _ex(*args):
        return Timestamp(Timestamp(datetime(*args)).value - 1)
    p = Period('2013-1-1', 'W-SAT')
    xp = _ex(2013, 1, 6)
    assert p.end_time == xp