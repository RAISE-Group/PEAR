def test_offset_freqstr(self, offset_types):
    offset = self._get_offset(offset_types)
    freqstr = offset.freqstr
    if freqstr not in ('<Easter>', '<DateOffset: days=1>', 'LWOM-SAT'):
        code = _get_offset(freqstr)
        assert offset.rule_code == code