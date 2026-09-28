def test_period_nat_comp(self):
    p_nat = Period('NaT', freq='D')
    p = Period('2011-01-01', freq='D')
    nat = Timestamp('NaT')
    t = Timestamp('2011-01-01')
    for left, right in [(p_nat, p), (p, p_nat), (p_nat, p_nat), (nat, t), (t, nat), (nat, nat)]:
        assert not left < right
        assert not left > right
        assert not left == right
        assert left != right
        assert not left <= right
        assert not left >= right