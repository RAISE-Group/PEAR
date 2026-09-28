@pytest.mark.slow
def test_dont_modify_colors(self):
    colors = ['r', 'g', 'b']
    pd.DataFrame(np.random.rand(10, 2)).plot(color=colors)
    assert len(colors) == 3