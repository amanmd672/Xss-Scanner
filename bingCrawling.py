import urllib


def web_page_source(file_path, site_url):
    n = 0

    file = open(file_path + "/get2.txt", 'w')

    for i in range(0, 50):
        z = i*10 + 1
        op1 = '&first=' + str(z)
        x = urllib.urlopen("https://www.bing.com/search?q="+site_url+op1).read()
        file.write(x)
        n += 1;
    print("\t+ {} added!".format(n))

    file.close()


def web_source_sorting(file_path):
    path = file_path + '/get2.txt'
    source_code = []
    source = []
    flag = False
    n = 0

    file = open(path, 'r+')

    while True:
        lines = file.readlines()
        if not lines:
            break
        for line in lines:
            source_code.append(line)

    for line in source_code:
        for word in line:
            if flag:
                source.append('\n')
                flag = False
            source.append(word)
            if '>' == word:
                n += 1
                flag = True

    str1 = ''.join(map(str, source))

    x = [y for y in (x.strip() for x in str1.splitlines()) if y]

    urls = []

    for line in x:
        if '<a href="http' in line:
            start = line.find('<a href="http') + 9
            end = line.find('"', start)
            urls.append(line[start:end])

    upload = open(file_path+'/get1.txt', 'a')

    for line in urls:
        upload.write(line)

    upload.close()

    print("done")

path = 'https-auth_idocker_hacking-lab_com.txt'
web_source_sorting(path)

# web_page_source(file_path, site_url)

