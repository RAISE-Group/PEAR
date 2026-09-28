@pytest.mark.slow
def test_secondary_bar_frame(self):
    df = DataFrame(np.random.randn(5, 3), columns=['a', 'b', 'c'])
    axes = df.plot(kind='bar', secondary_y=['a', 'c'], subplots=True)
    assert axes[0].get_yaxis().get_ticks_position() == 'right'
    assert axes[1].get_yaxis().get_ticks_position() == self.default_tick_position
    assert axes[2].get_yaxis().get_ticks_position() == 'right'