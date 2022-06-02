import urllib.request
# chardet 第三方库，用于检查网站的编码方式 
import chardet

def main():
    url = input('请输入URL：')

    response = urllib.request.urlopen(url)
    html = response.read()

    # 识别编码方式
    encode = chardet.detect(html)['encoding']
    if encode == 'GB2312':
        encode = 'GBK'

    print('该网页使用的编码是：%s'%encode)

if __name__ == '__main__':
    main()
