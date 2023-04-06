def find_all_dels(lenght):
    parties = [0, 0]
    minimal_delta = 1000
    for i in range(1, int(lenght**0.5)+1):
        if lenght % i == 0 and lenght//i - i < minimal_delta:
            minimal_delta = lenght//i - i
            parties[0] = i
            parties[1] = lenght//i
    if parties[1] == lenght:
        lenght += 1
        parties = find_all_dels(lenght)
    return parties
