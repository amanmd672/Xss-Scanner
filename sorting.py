import difflib
import sorting2

kw_sorted_1 = []
kw_sorted_2 = []
kw_sorted = []

words = ['?cat', '?q', 'to=', 'id=', 'l=', 'auto=', 'key=', 'keyword', 'email', 'emailstatus', 'search', 'text=', 'method', 'solovo', 'query', 'topic', 'register', 's=', 'language', 'result', 'page', 'sort=', 'obj=', 'object', 'list=', 'option', 'cmd=', 'login', 'listpage', 'address', 'query', 'complaint', 'category', 'url=', 'urlnext', 'originurl', 'targeturl', 'data', 'value', 'code=', 'market', 'mail', 'domain', 'title', 'message', 'msg=', 'txt=', 'event', 'c=', 'type', 'folder', 'cmd=', 'z=', 'searchstring', 'years', 'tag=', 'max=', 'from=', 'feedback', 'vote=', 'url=', 'id=', 'sid=', 'catid=', 'r=', 'pid=', 'course', 'course_id', 'errmsg', 'site', 'ref=', 'session', 'search_keyword', 'function', 'by=', 'buy_do', 'task', 'search', 'mid=']


def fun(file_path):
    with open(file_path + "get1.txt") as urls_test:

        url = []
        del_url = []
        real_url = []

        print("File opened!, working on it...")

        for line in urls_test:
            url.append(line)

        for i in range(0, len(url)-1):
            s1 = ''.join(url[i])
            compare_str_1 = s1.find('=')
            x = s1[:compare_str_1]

            s2 = ''.join(url[i+1])
            compare_str_2 = s2.find('=')
            y = s2[:compare_str_2]

            r = difflib.SequenceMatcher(isjunk=None, a=x, b=y)
            ratio = r.ratio()*100
            if ratio <= 95:
                real_url.append(url[i])
            else:
                del_url.append(url[i])

        real_url.append(url[len(url)-1])

    for i in range(0, len(real_url)):
        for j in range(0, len(words)):
            if words[j] in real_url[i]:
                kw_sorted_1.append(real_url[i])
                break
            else:
                kw_sorted_2.append(real_url[i])
                break

    kw_sorted = kw_sorted_1 + kw_sorted_2

    print(len(kw_sorted))

    upload = open(file_path+'get_updated.txt', 'w')

    for line in kw_sorted:
        upload.write(line)
        print(line)

    upload.close()

    #sorting2.sort_2(file_path)

    print("\n\t\t\t\tDone!")

