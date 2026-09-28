@pytest.mark.slow
def test_x_string_values_ticks(self):
    df = pd.DataFrame({'sales': [3, 2, 3], 'visits': [20, 42, 28], 'day': ['Monday', 'Tuesday', 'Wednesday']})
    ax = df.plot.area(x='day')
    ax.set_xlim(-1, 3)
    xticklabels = [t.get_text() for t in ax.get_xticklabels()]
    labels_position = dict(zip(xticklabels, ax.get_xticks()))
    assert labels_position['Monday'] == 0.0
    assert labels_position['Tuesday'] == 1.0
    assert labels_position['Wednesday'] == 2.0