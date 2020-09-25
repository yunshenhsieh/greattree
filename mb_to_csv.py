import os
from bs4 import BeautifulSoup
if os.path.exists(r'D:\demo\demo.txt'):
    input_path=r'D:\demo\demo.txt'
    output_path=''
    with open(input_path, 'r', encoding='utf-8')as f:
        tmp = f.read()
    soup = BeautifulSoup(tmp, 'html.parser')
    data = soup.select('td')
    data = [item.text.replace('"', '').strip().replace("=", '').strip() for item in data]
    data = [data[item:item + 12] for item in range(0, len(data), 12)]
    for item in data:
        with open(output_path, 'a', encoding='utf-8')as f:
            s_tmp = ''
            for i in item:
                s_tmp += i + r','
            f.write(s_tmp[:-1] + '\n')
    os.remove(input_path)
else:
    print('no file')