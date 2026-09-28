@classmethod
def _convert_to_protection(cls, protection_dict):
    """
        Convert ``protection_dict`` to an openpyxl v2 Protection object.
        Parameters
        ----------
        protection_dict : dict
            A dict with zero or more of the following keys.
                'locked'
                'hidden'
        Returns
        -------
        """
    from openpyxl.styles import Protection
    return Protection(**protection_dict)