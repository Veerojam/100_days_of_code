

def format_name(f_name, l_name):
    normalized_fname = f_name.title()
    normalized_lname = l_name.title()
    return f"{normalized_fname} {normalized_lname}"

names = format_name("jAcK", "BAUER")
print(names)