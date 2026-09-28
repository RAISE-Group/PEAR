def test_bar_align_zero_pos_and_neg(self):
    df = pd.DataFrame({'A': [-10, 0, 20, 90]})
    result = df.style.bar(align='zero', color=['#d65f5f', '#5fba7d'], width=90)._compute().ctx
    expected = {(0, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 40.0%, #d65f5f 40.0%, #d65f5f 45.0%, transparent 45.0%)'], (1, 0): ['width: 10em', ' height: 80%'], (2, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 45.0%, #5fba7d 45.0%, #5fba7d 55.0%, transparent 55.0%)'], (3, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 45.0%, #5fba7d 45.0%, #5fba7d 90.0%, transparent 90.0%)']}
    assert result == expected