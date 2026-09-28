def test_compare_tick(self, tick_classes):
    cls = tick_classes
    off = cls(4)
    td = off.delta
    assert isinstance(td, Timedelta)
    assert td == off
    assert not td != off
    assert td <= off
    assert td >= off
    assert not td < off
    assert not td > off
    assert not td == 2 * off
    assert td != 2 * off
    assert td <= 2 * off
    assert td < 2 * off
    assert not td >= 2 * off
    assert not td > 2 * off