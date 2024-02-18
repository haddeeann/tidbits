def build_pyramid(pyramid_height):
    rows = 1
    numbers_str = 1
    row_ends = []
    while rows <= pyramid_height:
        str_builder = rows
        build = ''
        while str_builder > 0:
            build += str(numbers_str) + ' '
            if str_builder == 1:
                row_ends.append(str(numbers_str))
            str_builder -= 1
            numbers_str += 1
        rows += 1
    return row_ends


def decode(message_file):
    line_count = 0
    with open(message_file) as f:
        key_value_dict = {}
        for s in f.read().split('\n'):
            if s:
                line_count += 1
                key_value_arr = s.split(' ')
                key = key_value_arr[0]
                value = key_value_arr[1]
                key_value_dict[key] = value

    row_end_arr = build_pyramid(pyramid_height=line_count)
    answer_arr = []
    for row_end in row_end_arr:
        if row_end in key_value_dict:
            word = key_value_dict[row_end]
            answer_arr.append(word)

    return ' '.join(answer_arr)


print(decode('coding_qual_input.txt'))
