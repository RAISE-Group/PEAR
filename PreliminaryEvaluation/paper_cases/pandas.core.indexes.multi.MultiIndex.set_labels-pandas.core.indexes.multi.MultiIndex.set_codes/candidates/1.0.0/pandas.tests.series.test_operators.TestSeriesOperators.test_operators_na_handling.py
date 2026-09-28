def test_operators_na_handling(self):
    from decimal import Decimal
    from datetime import date
    s = Series([Decimal('1.3'), Decimal('2.3')], index=[date(2012, 1, 1), date(2012, 1, 2)])
    result = s + s.shift(1)
    result2 = s.shift(1) + s
    assert isna(result[0])
    assert isna(result2[0])