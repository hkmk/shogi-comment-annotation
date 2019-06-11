import sys

def decode(kif, label):
    output = ''
    ki = 0
    li = 0
    while ki < len(kif):
        if len(label) <= li:
            print([c for c in kif])
            print(output)
            print(label)
            exit(0)
        if label[li] == '〜/add':
            output += '〜/O/O '
            li += 1
            continue
        if kif[ki] == '\u3000' or kif[ki] == ' ':
            ki += 1
            continue
        output += kif[ki]
        if label[li] is not None:
            output += '/'+label[li] + ' '
        ki += 1
        li += 1
    return '*'+output.rstrip()

def decode_file(kif_filename, label_filename):
    label = []
    with open(label_filename, 'r', encoding='utf-8') as l_f:
        for l in l_f.readlines():
            label.append([ w if w != 'None' else None for w in l.split() ])

    li = 0
    with open(kif_filename, 'r', encoding='utf-8') as kif:
        for l in kif.readlines():
            if not l.startswith('*'):
                print(l.rstrip())
                continue
            l_kif_one = l.strip()
            l_kif = l_kif_one[1:]
            if l_kif.endswith('棋'):
                l_kif_pre = l_kif
                continue
            if l_kif.startswith('聖'):
                l_kif = l_kif_pre + l_kif

            print(decode(l_kif, label[li]))
            li += 1

if __name__=='__main__':
    argvs = sys.argv
    argc = len(argvs)

    if argc != 3:
        sys.stderr.write('Usage: python decoder.py kif_filename label_filename\n')
        exit(0)

    kif_filename = argvs[1]
    label_filename = argvs[2]

    decode_file(kif_filename, label_filename)
