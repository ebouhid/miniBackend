def del_by_name(name: str, petList: list):
    return [pet for pet in petList if pet["name"] != name]