def _add_offset(self, other):
    assert not isinstance(other, Tick)
    base = libfrequencies.get_base_alias(other.rule_code)
    if base != self.freq.rule_code:
        raise raise_on_incompatible(self, other)
    result = super()._add_timedeltalike_scalar(other.n)
    return type(self)(result, freq=self.freq)