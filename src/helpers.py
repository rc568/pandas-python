def array_string_to_string(string_like_array: str):
    if string_like_array == '[]':
        return []
    images_list = list(map(lambda x: x.strip()[1:-1], string_like_array[1:-1].split(',')))
    return images_list
