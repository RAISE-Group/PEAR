def test_bar_align_mid_pos_and_neg(self):
    df = pd.DataFrame({'A': [-10, 0, 20, 90]})
    result = df.style.bar(align='mid', color=['#d65f5f', '#5fba7d'])._compute().ctx
    expected = {(0, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,#d65f5f 10.0%, transparent 10.0%)'], (1, 0): ['width: 10em', ' height: 80%'], (2, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 10.0%, #5fba7d 10.0%, #5fba7d 30.0%, transparent 30.0%)'], (3, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 10.0%, #5fba7d 10.0%, #5fba7d 100.0%, transparent 100.0%)']}
    assert result == expected