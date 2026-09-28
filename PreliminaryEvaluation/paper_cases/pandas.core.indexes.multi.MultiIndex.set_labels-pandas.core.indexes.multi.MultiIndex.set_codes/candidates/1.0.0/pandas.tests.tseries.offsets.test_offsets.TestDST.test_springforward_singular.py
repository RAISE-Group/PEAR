def test_springforward_singular(self):
    for tz, utc_offsets in self.timezone_utc_offsets.items():
        hrs_pre = utc_offsets['utc_offset_standard']
        self._test_all_offsets(n=1, tstart=self._make_timestamp(self.ts_pre_springfwd, hrs_pre, tz), expected_utc_offset=None)