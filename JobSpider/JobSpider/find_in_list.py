def find_in_list(self, key, list_name):
    for i in range(0, len(list_name)):
        value = list_name.strip().split("|")[i].strip()
        if key in value:
            return value