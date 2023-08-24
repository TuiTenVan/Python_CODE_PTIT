def generate_strings(N, current_string, count_a, count_b, count_c):
    if len(current_string) > 0:
        if count_a == 1 and count_b <= count_a and count_b <= count_c:
            print(current_string)

    if len(current_string) >= N:
        return

    generate_strings(N, current_string + 'A', count_a + 1, count_b, count_c)
    generate_strings(N, current_string + 'B', count_a, count_b + 1, count_c)
    generate_strings(N, current_string + 'C', count_a, count_b, count_c + 1)

N = int(input())
generate_strings(N, '', 0, 0, 0)
