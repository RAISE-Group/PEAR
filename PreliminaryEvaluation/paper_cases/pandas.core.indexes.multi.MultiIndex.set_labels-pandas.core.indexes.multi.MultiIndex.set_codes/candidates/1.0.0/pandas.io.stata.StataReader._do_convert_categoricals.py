def _do_convert_categoricals(self, data, value_label_dict, lbllist, order_categoricals):
    """
        Converts categorical columns to Categorical type.
        """
    value_labels = list(value_label_dict.keys())
    cat_converted_data = []
    for col, label in zip(data, lbllist):
        if label in value_labels:
            cat_data = Categorical(data[col], ordered=order_categoricals)
            categories = []
            for category in cat_data.categories:
                if category in value_label_dict[label]:
                    categories.append(value_label_dict[label][category])
                else:
                    categories.append(category)
            try:
                cat_data.categories = categories
            except ValueError:
                vc = Series(categories).value_counts()
                repeats = list(vc.index[vc > 1])
                repeats = '-' * 80 + '\n' + '\n'.join(repeats)
                msg = f'\nValue labels for column {col} are not unique. These cannot be converted to\npandas categoricals.\n\nEither read the file with `convert_categoricals` set to False or use the\nlow level interface in `StataReader` to separately read the values and the\nvalue_labels.\n\nThe repeated labels are:\n{repeats}\n'
                raise ValueError(msg)
            cat_data = Series(cat_data, index=data.index)
            cat_converted_data.append((col, cat_data))
        else:
            cat_converted_data.append((col, data[col]))
    data = DataFrame.from_dict(dict(cat_converted_data))
    return data