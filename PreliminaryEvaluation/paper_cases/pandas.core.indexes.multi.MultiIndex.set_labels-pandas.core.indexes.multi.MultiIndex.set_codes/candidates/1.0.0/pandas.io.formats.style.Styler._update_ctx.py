def _update_ctx(self, attrs):
    """
        Update the state of the Styler.

        Collects a mapping of {index_label: ['<property>: <value>']}.

        attrs : Series or DataFrame
        should contain strings of '<property>: <value>;<prop2>: <val2>'
        Whitespace shouldn't matter and the final trailing ';' shouldn't
        matter.
        """
    for row_label, v in attrs.iterrows():
        for col_label, col in v.items():
            i = self.index.get_indexer([row_label])[0]
            j = self.columns.get_indexer([col_label])[0]
            for pair in col.rstrip(';').split(';'):
                self.ctx[i, j].append(pair)