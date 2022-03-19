"""Functions to help with module hygiene!

The main function exported is `cleanup`. The `cleanup`
function generates code which, upon execution, will
`del` every `local` variable that is not in some 
pre-defined list of `export` variables.
"""

def cleanup(export: str = "__export__") -> str:
    """ Generate code to clean up the current namespace!
    
    Usage: `exec(cleanup())`
    """
    from textwrap import dedent
    return dedent(
        f"""
        for variable in locals().copy():
            if variable != "{export}" and variable not in {export}:
                del locals()[variable]
        del variable, {export}
        """
    )