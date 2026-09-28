def render(self, **kwargs):
    """
        Render the built up styles to HTML.

        Parameters
        ----------
        **kwargs
            Any additional keyword arguments are passed
            through to ``self.template.render``.
            This is useful when you need to provide
            additional variables for a custom template.

        Returns
        -------
        rendered : str
            The rendered HTML.

        Notes
        -----
        ``Styler`` objects have defined the ``_repr_html_`` method
        which automatically calls ``self.render()`` when it's the
        last item in a Notebook cell. When calling ``Styler.render()``
        directly, wrap the result in ``IPython.display.HTML`` to view
        the rendered HTML in the notebook.

        Pandas uses the following keys in render. Arguments passed
        in ``**kwargs`` take precedence, so think carefully if you want
        to override them:

        * head
        * cellstyle
        * body
        * uuid
        * precision
        * table_styles
        * caption
        * table_attributes
        """
    self._compute()
    d = self._translate()
    trimmed = [x for x in d['cellstyle'] if any((any(y) for y in x['props']))]
    d['cellstyle'] = trimmed
    d.update(kwargs)
    return self.template.render(**d)