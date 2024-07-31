print("---------------------\nName: Owen Jones \nSchool: Cardiff High School\n---------------------\n")

def generate_fib_seq(lim):
    seq = [1, 2]
    i = 0
    while seq[-1]<lim:
        seq.append(seq[i] + seq[i+1])
        i += 1
    return seq


def make_zeckendorf_rep(seq):
    inp = int(input("number from 1-1,000,000: "))
    if inp > 1_000_000:
        print("number must be between 1 and 1000000 (inclusive)")
        return

    rep_list = []
    for i in range(len(seq)):
        if inp - seq[len(seq)-i-1] < 0:
            continue
        else:
            inp -= seq[len(seq)-i-1]
            rep_list.append(str(seq[len(seq)-i-1]))

    print(" ".join(rep_list))


make_zeckendorf_rep(generate_fib_seq(1_000_000))

