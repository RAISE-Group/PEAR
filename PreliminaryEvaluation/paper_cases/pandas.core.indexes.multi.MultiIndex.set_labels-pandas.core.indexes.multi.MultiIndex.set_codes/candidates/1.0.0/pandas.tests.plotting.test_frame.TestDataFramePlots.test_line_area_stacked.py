def test_line_area_stacked(self):
    with tm.RNGContext(42):
        df = DataFrame(rand(6, 4), columns=['w', 'x', 'y', 'z'])
        neg_df = -df
        sep_df = DataFrame({'w': rand(6), 'x': rand(6), 'y': -rand(6), 'z': -rand(6)})
        mixed_df = DataFrame(randn(6, 4), index=list(string.ascii_letters[:6]), columns=['w', 'x', 'y', 'z'])
        for kind in ['line', 'area']:
            ax1 = _check_plot_works(df.plot, kind=kind, stacked=False)
            ax2 = _check_plot_works(df.plot, kind=kind, stacked=True)
            self._compare_stacked_y_cood(ax1.lines, ax2.lines)
            ax1 = _check_plot_works(neg_df.plot, kind=kind, stacked=False)
            ax2 = _check_plot_works(neg_df.plot, kind=kind, stacked=True)
            self._compare_stacked_y_cood(ax1.lines, ax2.lines)
            ax1 = _check_plot_works(sep_df.plot, kind=kind, stacked=False)
            ax2 = _check_plot_works(sep_df.plot, kind=kind, stacked=True)
            self._compare_stacked_y_cood(ax1.lines[:2], ax2.lines[:2])
            self._compare_stacked_y_cood(ax1.lines[2:], ax2.lines[2:])
            _check_plot_works(mixed_df.plot, stacked=False)
            with pytest.raises(ValueError):
                mixed_df.plot(stacked=True)
            df2 = df.set_index(df.index + 1)
            _check_plot_works(df2.plot, kind=kind, logx=True, stacked=True)