@pytest.mark.slow
def test_hist_layout(self):
    df = self.hist_df
    with pytest.raises(ValueError):
        df.height.hist(layout=(1, 1))
    with pytest.raises(ValueError):
        df.height.hist(layout=[1, 1])