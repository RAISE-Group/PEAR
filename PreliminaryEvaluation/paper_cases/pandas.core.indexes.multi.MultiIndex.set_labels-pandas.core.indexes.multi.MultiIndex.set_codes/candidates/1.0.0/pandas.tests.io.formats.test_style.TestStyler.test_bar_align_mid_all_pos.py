def test_bar_align_mid_all_pos(self):
    df = pd.DataFrame({'A': [10, 20, 50, 100]})
    result = df.style.bar(align='mid', color=['#d65f5f', '#5fba7d'])._compute().ctx
    expected = {(0, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,#5fba7d 10.0%, transparent 10.0%)'], (1, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,#5fba7d 20.0%, transparent 20.0%)'], (2, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,#5fba7d 50.0%, transparent 50.0%)'], (3, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,#5fba7d 100.0%, transparent 100.0%)']}
    assert result == expected