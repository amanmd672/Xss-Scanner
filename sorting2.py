import difflib
import os


def sort_2(file_path):

    url = []
    del_url = []
    real_url = []

    with open(file_path + "get.txt") as urls:

        print("File opened!, working on it...")

        for line in urls:
            url.append(line)


    for i in range(0, len(url)-1):

        start = 0
        end = 0
        flag1 = False

        for j in range(len(url[i])-1, 0-1, -1):
            if url[i][j] == '=' and not flag1:
                start = j
                flag1 = True
            if url[i][j] == '?':
                end = j

        s1 = ''.join(url[i][end:start])

        start = 0
        end = 0
        flag1 = False

        for j in range(len(url[i+1])-1, 0-1, -1):
            if url[i+1][j] == '=' and not flag1:
                start = j
                flag1 = True
            if url[i+1][j] == '?':
                end = j

        s2 = ''.join(url[i+1][end:start])

        r = difflib.SequenceMatcher(isjunk=None, a=s1, b=s2)
        ratio = r.ratio()*100

        if ratio >= 94:
            del_url.append(url[i])
        else:
            real_url.append(url[i])

    upload = open(file_path+'get_updated.txt', 'w')

    for line in real_url:
        upload.write(line)


    upload.write(real_url[len(real_url)-1])

    upload.close

    print("\t*\tlen of del_url => {}".format(len(del_url)))
    print("\t*\tlen of real_url => {}".format(len(real_url)))
    print("\t*\tlen of url=> {}".format(len(url)))

    os.remove(file_path+'get1.txt')
    os.remove(file_path+'get.txt')
