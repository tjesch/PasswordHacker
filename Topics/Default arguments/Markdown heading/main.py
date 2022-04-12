def heading(text, level=1):
    return_text = ''
    if level > 6:
        level = 6
    elif level < 1:
        level = 1
    for x in range(level):
        return_text += '#'
    return_text = return_text + ' ' + text
    return return_text
