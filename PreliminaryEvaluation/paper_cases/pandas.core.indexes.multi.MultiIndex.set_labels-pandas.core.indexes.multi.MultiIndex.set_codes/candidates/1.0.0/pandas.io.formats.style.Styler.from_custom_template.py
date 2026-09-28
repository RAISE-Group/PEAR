@classmethod
def from_custom_template(cls, searchpath, name):
    """
        Factory function for creating a subclass of ``Styler``.

        Uses a custom template and Jinja environment.

        Parameters
        ----------
        searchpath : str or list
            Path or paths of directories containing the templates.
        name : str
            Name of your custom template to use for rendering.

        Returns
        -------
        MyStyler : subclass of Styler
            Has the correct ``env`` and ``template`` class attributes set.
        """
    loader = jinja2.ChoiceLoader([jinja2.FileSystemLoader(searchpath), cls.loader])

    class MyStyler(cls):
        env = jinja2.Environment(loader=loader)
        template = env.get_template(name)
    return MyStyler