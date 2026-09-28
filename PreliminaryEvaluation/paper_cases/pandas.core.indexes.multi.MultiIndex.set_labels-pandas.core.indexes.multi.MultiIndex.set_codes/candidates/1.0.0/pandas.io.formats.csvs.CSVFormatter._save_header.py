def _save_header(self):
    writer = self.writer
    obj = self.obj
    index_label = self.index_label
    cols = self.cols
    has_mi_columns = self.has_mi_columns
    header = self.header
    encoded_labels: List[str] = []
    has_aliases = isinstance(header, (tuple, list, np.ndarray, ABCIndexClass))
    if not (has_aliases or self.header):
        return
    if has_aliases:
        if len(header) != len(cols):
            raise ValueError(f'Writing {len(cols)} cols but got {len(header)} aliases')
        else:
            write_cols = header
    else:
        write_cols = cols
    if self.index:
        if index_label is not False:
            if index_label is None:
                if isinstance(obj.index, ABCMultiIndex):
                    index_label = []
                    for i, name in enumerate(obj.index.names):
                        if name is None:
                            name = ''
                        index_label.append(name)
                else:
                    index_label = obj.index.name
                    if index_label is None:
                        index_label = ['']
                    else:
                        index_label = [index_label]
            elif not isinstance(index_label, (list, tuple, np.ndarray, ABCIndexClass)):
                index_label = [index_label]
            encoded_labels = list(index_label)
        else:
            encoded_labels = []
    if not has_mi_columns or has_aliases:
        encoded_labels += list(write_cols)
        writer.writerow(encoded_labels)
    else:
        columns = obj.columns
        for i in range(columns.nlevels):
            col_line = []
            if self.index:
                col_line.append(columns.names[i])
                if isinstance(index_label, list) and len(index_label) > 1:
                    col_line.extend([''] * (len(index_label) - 1))
            col_line.extend(columns._get_level_values(i))
            writer.writerow(col_line)
        if encoded_labels and set(encoded_labels) != {''}:
            encoded_labels.extend([''] * len(columns))
            writer.writerow(encoded_labels)