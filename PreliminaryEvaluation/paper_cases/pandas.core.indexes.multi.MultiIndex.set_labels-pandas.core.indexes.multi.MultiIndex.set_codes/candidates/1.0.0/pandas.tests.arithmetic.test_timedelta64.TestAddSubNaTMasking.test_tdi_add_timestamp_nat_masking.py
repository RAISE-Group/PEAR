def test_tdi_add_timestamp_nat_masking(self):
    tdinat = pd.to_timedelta(['24658 days 11:15:00', 'NaT'])
    tsneg = Timestamp('1950-01-01')
    ts_neg_variants = [tsneg, tsneg.to_pydatetime(), tsneg.to_datetime64().astype('datetime64[ns]'), tsneg.to_datetime64().astype('datetime64[D]')]
    tspos = Timestamp('1980-01-01')
    ts_pos_variants = [tspos, tspos.to_pydatetime(), tspos.to_datetime64().astype('datetime64[ns]'), tspos.to_datetime64().astype('datetime64[D]')]
    for variant in ts_neg_variants + ts_pos_variants:
        res = tdinat + variant
        assert res[1] is pd.NaT