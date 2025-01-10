import requests
from bs4 import BeautifulSoup

login_url = "http://localhost:8000/login/"
username = "admin"
password = "admin"

response_with_csrf_token = requests.get(login_url)
csrf_token_cookie = response_with_csrf_token.cookies
# print(csrf_token_cookie)
soup = BeautifulSoup(response_with_csrf_token.text, "html.parser")
csrf_middleware_token_obj = soup.select("input[name=csrfmiddlewaretoken]")[0]
# print(csrf_middleware_token_obj)

csrf_mtkn_name = csrf_middleware_token_obj.get("name")
csrf_mtkn_value = csrf_middleware_token_obj.get("value")

form_data = {
    csrf_mtkn_name: csrf_mtkn_value,
    "username": username,
    "password": password,
}

result = requests.post(
    login_url, cookies=csrf_token_cookie, data=form_data, allow_redirects=False
)

print(result.cookies)
csrf_cookie_value = result.cookies.get("csrftoken")
sessionid_cookie_value = result.cookies.get("sessionid")

print(f"csrftoken={csrf_cookie_value}")
print(f"sessionid={sessionid_cookie_value}")

"""
zap.replacer.add_rule(
    description="Add session cookies",
    enabled=True,
    matchtype="REQ_HEADER",
    matchregex=False,
    matchstring="Cookie",
    replacement=f"sessionid={sessionid_cookie_value}; csrftoken={csrf_cookie_value}"
)
"""
