#use urlopen to read data from websites

from urllib.request import urlopen
link = 'http://python.org/'

def get_html():
    try:
        http_rsp = urlopen(link)
        print('HTTP RSP:\n'+str(http_rsp))
        html = http_rsp.read()
        print('HTML:\n'+str(html))
        html_decoded = html.decode()
        print('HTML decoded:\n'+str(html_decoded))
    except Exception as ex:
        print('Failed to get HTML! \n\n'+str(ex))
    else:
        return html_decoded
