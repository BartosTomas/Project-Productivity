import data

def save(key, val):
    key = key
    val = val
    if key in data.Text_fields:
        return
    else:
        data.Text_fields[key] = val

save("name", "něco")