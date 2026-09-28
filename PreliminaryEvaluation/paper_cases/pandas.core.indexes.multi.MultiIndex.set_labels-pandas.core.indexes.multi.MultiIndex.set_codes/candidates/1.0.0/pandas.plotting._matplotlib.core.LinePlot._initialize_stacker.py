@classmethod
def _initialize_stacker(cls, ax, stacking_id, n):
    if stacking_id is None:
        return
    if not hasattr(ax, '_stacker_pos_prior'):
        ax._stacker_pos_prior = {}
    if not hasattr(ax, '_stacker_neg_prior'):
        ax._stacker_neg_prior = {}
    ax._stacker_pos_prior[stacking_id] = np.zeros(n)
    ax._stacker_neg_prior[stacking_id] = np.zeros(n)