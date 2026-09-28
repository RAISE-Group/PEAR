def test_td64arr_div_nat_invalid(self, box_with_array):
    rng = timedelta_range('1 days', '10 days', name='foo')
    rng = tm.box_expected(rng, box_with_array)
    with pytest.raises(TypeError, match='unsupported operand type'):
        rng / pd.NaT
    with pytest.raises(TypeError, match='Cannot divide NaTType by'):
        pd.NaT / rng