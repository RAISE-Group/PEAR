def test_flat_stays_flat(self):
    recs = [dict(flat1=1, flat2=2), dict(flat1=3, flat2=4)]
    result = nested_to_record(recs)
    expected = recs
    assert result == expected