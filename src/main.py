def hello(name="GitHub Actions"):
    """
    Renvoie une salutation personnalisée.
    """
    if not isinstance(name, str):
        raise TypeError("Le nom doit être une chaîne de caractères")
    return f"Hello, {name}!"
