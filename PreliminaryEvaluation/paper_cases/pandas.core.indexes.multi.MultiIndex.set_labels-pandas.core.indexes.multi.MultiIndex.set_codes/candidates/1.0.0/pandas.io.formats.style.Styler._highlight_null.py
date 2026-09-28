@staticmethod
def _highlight_null(v, null_color):
    return f'background-color: {null_color}' if pd.isna(v) else ''