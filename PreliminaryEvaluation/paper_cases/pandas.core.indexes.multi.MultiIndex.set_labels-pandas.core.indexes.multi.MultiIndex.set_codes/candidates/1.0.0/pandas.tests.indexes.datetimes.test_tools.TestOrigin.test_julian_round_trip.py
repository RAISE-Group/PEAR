def test_julian_round_trip(self):
    result = pd.to_datetime(2456658, origin='julian', unit='D')
    assert result.to_julian_date() == 2456658
    with pytest.raises(ValueError):
        pd.to_datetime(1, origin='julian', unit='D')