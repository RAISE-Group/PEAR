@classmethod
def _get_ax_layer(cls, ax, primary=True):
    """get left (primary) or right (secondary) axes"""
    if primary:
        return getattr(ax, 'left_ax', ax)
    else:
        return getattr(ax, 'right_ax', ax)