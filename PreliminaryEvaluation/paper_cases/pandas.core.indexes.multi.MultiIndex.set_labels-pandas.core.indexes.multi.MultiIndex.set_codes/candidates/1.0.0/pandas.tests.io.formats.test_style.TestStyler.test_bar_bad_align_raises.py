def test_bar_bad_align_raises(self):
    df = pd.DataFrame({'A': [-100, -60, -30, -20]})
    with pytest.raises(ValueError):
        df.style.bar(align='poorly', color=['#d65f5f', '#5fba7d'])