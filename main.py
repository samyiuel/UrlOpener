import webbrowser

urls = input('Enter the url list: ')
# https://github.com/ https://www.google.com/ https://gmail.com/

url_list = list(urls.split(" "))

for url in url_list:
    webbrowser.open(url)
