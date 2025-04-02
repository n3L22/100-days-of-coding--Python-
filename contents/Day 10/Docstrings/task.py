#to make a dockstring to explain the function what does it do
#it is a way to document a function 
def format_name(name, surname):
    """Capitalize

    Args:
        name (str): Capitalise first letter
        surname (str): Capitalise first letter

    Returns:
        str: Concatinate the together
    """
    f_name = name.capitalize()
    f_sname = surname.capitalize()
    return f"{f_name} {f_sname}"


print(format_name("nela", "rakipaj"))
