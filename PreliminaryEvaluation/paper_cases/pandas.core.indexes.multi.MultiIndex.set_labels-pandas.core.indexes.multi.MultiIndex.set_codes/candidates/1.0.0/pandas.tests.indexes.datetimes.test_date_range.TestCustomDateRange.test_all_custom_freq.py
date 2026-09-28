@pytest.mark.parametrize('freq', [freq for freq in prefix_mapping if freq.startswith('C')])
def test_all_custom_freq(self, freq):
    bdate_range(START, END, freq=freq, weekmask='Mon Wed Fri', holidays=['2009-03-14'])
    bad_freq = freq + 'FOO'
    msg = 'invalid custom frequency string: {freq}'
    with pytest.raises(ValueError, match=msg.format(freq=bad_freq)):
        bdate_range(START, END, freq=bad_freq)