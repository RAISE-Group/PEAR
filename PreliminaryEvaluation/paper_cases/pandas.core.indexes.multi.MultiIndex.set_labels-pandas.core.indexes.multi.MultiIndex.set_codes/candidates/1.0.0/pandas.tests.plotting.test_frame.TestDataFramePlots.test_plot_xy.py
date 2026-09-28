@pytest.mark.slow
def test_plot_xy(self):
    df = self.tdf
    self._check_data(df.plot(x=0, y=1), df.set_index('A')['B'].plot())
    self._check_data(df.plot(x=0), df.set_index('A').plot())
    self._check_data(df.plot(y=0), df.B.plot())
    self._check_data(df.plot(x='A', y='B'), df.set_index('A').B.plot())
    self._check_data(df.plot(x='A'), df.set_index('A').plot())
    self._check_data(df.plot(y='B'), df.B.plot())
    df.columns = np.arange(1, len(df.columns) + 1)
    self._check_data(df.plot(x=1, y=2), df.set_index(1)[2].plot())
    self._check_data(df.plot(x=1), df.set_index(1).plot())
    self._check_data(df.plot(y=1), df[1].plot())
    ax = df.plot(x=1, y=2, title='Test', figsize=(16, 8))
    self._check_text_labels(ax.title, 'Test')
    self._check_axes_shape(ax, axes_num=1, layout=(1, 1), figsize=(16.0, 8.0))