def array_of_names(persons):
    names = []
    for first_name, last_name in persons.items():
        names.append(f"{first_name} {last_name}")
    return names


persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))