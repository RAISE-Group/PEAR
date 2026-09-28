def test_bar_align_mid_all_neg(self):
    df = pd.DataFrame({'A': [-100, -60, -30, -20]})
    result = df.style.bar(align='mid', color=['#d65f5f', '#5fba7d'])._compute().ctx
    expected = {(0, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,#d65f5f 100.0%, transparent 100.0%)'], (1, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 40.0%, #d65f5f 40.0%, #d65f5f 100.0%, transparent 100.0%)'], (2, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 70.0%, #d65f5f 70.0%, #d65f5f 100.0%, transparent 100.0%)'], (3, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 80.0%, #d65f5f 80.0%, #d65f5f 100.0%, transparent 100.0%)']}
    assert result == expected