import os
import sorting
import base64
import multithreading_testing

delete_str1 = '<request'
delete_str2 = ['<request base64="true"><![CDATA[', ']]></request>']
delete_str3 = ['''\\r\\n''', "b'", "'"]

url_type_get = 'GET '
url_type_post = 'POST '
post_data = []

requests = []
url = []
required_url = []
req_url_get = []
req_url_post = []
req_post_url = []
domain_name = ''
site_url = ''
data = []
urls_key = []
sorted_urls=''

def main():
    url = input('Enter the url => ')
    start = url.find('://') + 3
    url_name = url[start:]

    file_name = url_name
    file_path = 'C:\\Users\\AmanMudholkar\\Documents\\'+file_name+'\\'
    ensure_dir(file_path)

    db_file_name = domain(url)
    print(db_file_name)
    db_file_path = 'C:\\Users\\AmanMudholkar\\Documents\\'+db_file_name+'.txt'

    getting_links(db_file_path, url, file_path)

    start_url = url.find('www.') + 4
    site_url = ''.join(url[start_url:])

    sorted_urls=file_path+'get_updated.txt'
    multithreading_testing.start_engine(sorted_urls)
    return site_url


def domain(file_name):
    domain_name = file_name.replace('://', '-')

    domain_name = domain_name.replace('.', '_')

    return domain_name


def post_data_fun(line):
    data = [line]

    str = ''.join(data)

    return str.splitlines()[-1]


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("path already exist")


def getting_links(db_file_path, url1, file_path):
    with open(db_file_path, 'r') as links:
        for line in links:
            if delete_str1 in line:
                requests.append(line)

        for line in requests:
            for word in delete_str2:
                line = line.replace(word, '')
            url.append(line)

        for i in url:
            url_now = i
            url_decode = base64.b64decode(url_now)

            decoded_url = [str(url_decode)]

            for line in decoded_url:
                for word in delete_str3:
                    line = line.replace(word, '\n')
                required_url.append(line)

        for line in required_url:
            if url_type_get in line:
                start = line.find("GET ") + 4
                end = line.find('HTTP', start)
                req_url_get.append(url1+line[start:end])

            elif url_type_post in line:
                post_data.append(line)
                start = line.find("POST ") + 5
                end = line.find('HTTP', start)
                req_url_post.append(url1+line[start:end])

        for line in req_url_get:
            if '?' in line:
                urls_key.append(line)

    print("get1 => {}".format(len(urls_key)))

    upload_get = open(file_path+"get1.txt", 'w')

    for line in urls_key:
        upload_get.write(line)
        upload_get.write("\n")

    upload_get.close()

    for line in post_data:
        data.append(post_data_fun(line))

    for i in range(0, min(len(data), len(req_post_url))):
        req_post_url.append(req_url_post[i] + "\n" + data[i])

    upload_post = open(file_path+"post.txt", 'w')

    for line in req_post_url:
        upload_post.write(line)
        upload_post.write("\n")

    upload_post.close()

    sorting.fun(file_path+'\\')

    return


# https:/azure.microsoft.com