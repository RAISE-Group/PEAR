def test_render_empty_dfs(self):
    empty_df = DataFrame()
    es = Styler(empty_df)
    es.render()
    DataFrame(columns=['a']).style.render()
    DataFrame(index=['a']).style.render()