def save_path(id, filename):
    return f'./output/{id}/{filename}'


def save_file(id, filename, content):
    f = open(save_path(id, filename), 'w')
    f.write(content)
    f.close()
