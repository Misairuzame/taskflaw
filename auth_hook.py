# import subprocess
# import sys
# import requests

""" try:
    import bs4
except ImportError:
    # Se non è installato, installalo con pip
    print(f"Installazione di beautifulsoup4 in corso...")
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "beautifulsoup4",
            "--break-system-packages",
        ]
    )
    import os

    print("Riavvio dello script...")
    os.execv(sys.executable, [sys.executable] + sys.argv)

BeautifulSoup = bs4.BeautifulSoup """

from zapv2 import ZAPv2


def zap_started(zap: ZAPv2, target):
    print("The target is:", target)

    zap.urlopen(target)
    # zap.script.load(
    #    "LogMessages.js", "httpsender", "Oracle Nashorn", "/zap/wrk/LogMessages.js"
    # )
    # zap.script.enable("LogMessages.js")

    login_url = f"{target}/login/"
    username = "admin"
    password = "admin"

    """ response_with_csrf_token = requests.get(login_url)
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
    print(f"sessionid={sessionid_cookie_value}") """

    # zap.replacer.add_rule(
    #     description="Add session cookies",
    #     enabled=True,
    #     matchtype="REQ_HEADER",
    #     matchregex=False,
    #     matchstring="Cookie",
    #     replacement=f"csrftoken={csrf_cookie_value}; sessionid={sessionid_cookie_value}",
    #     #replacement=f"csrftoken={csrf_cookie_value}",
    # )

    context_name = "Default Context"
    zap.context.new_context(context_name)
    print(zap.context.context_list)
    context_id = 1

    # logged_out_regex = "(Please enter a correct username and password)|(CSRF verification failed)|(Page not found)"
    logged_out_regex = (
        "(Please enter a correct username and password)|(CSRF verification failed)"
    )
    zap.authentication.set_logged_out_indicator(context_id, logged_out_regex)
    logged_in_regex = "(Hello )|(Title:(.|\n|\r)*Description:)|(Are you sure you want to delete this note)"
    zap.authentication.set_logged_in_indicator(context_id, logged_in_regex)

    zap.context.include_in_context(context_name, f"{target}.*")
    zap.context.include_in_context(context_name, f"{target}/note-create.*")
    # zap.context.include_in_context(context_name, f"{target}/note-delete.*")
    zap.context.include_in_context(context_name, f"{target}/note-update.*")
    zap.context.include_in_context(context_name, f"{target}/?search-area=.*")
    zap.context.exclude_from_context(context_name, f"{target}/note-delete.*")
    zap.context.exclude_from_context(context_name, ".*logout.*")

    zap.replacer.add_rule(
        description="Remove 'complete=on' from POST data",
        enabled=True,
        matchtype="REQ_BODY_STR",
        matchregex=False,
        matchstring="&complete=on",
        replacement="",
    )

    # zap.replacer.add_rule(
    #     description="Keep current value of csrfmiddlewaretoken from POST data",
    #     enabled=True,
    #     matchtype="REQ_BODY_STR",
    #     matchregex=True,
    #     matchstring="(csrfmiddlewaretoken=\S+?)&",
    #     replacement="$1&",
    # )

    # zap.replacer.add_rule(
    #     description="Keep current value of csrfmiddlewaretoken from POST data (2)",
    #     enabled=True,
    #     matchtype="REQ_BODY_STR",
    #     matchregex=True,
    #     matchstring="(csrfmiddlewaretoken=\S+?)$",
    #     replacement="$1",
    # )

    import urllib

    print(zap.acsrf.option_tokens_names)

    login_request_data = (
        "csrfmiddlewaretoken=A_CSRF_TOKEN&username={%username%}&password={%password%}"
    )
    form_based_config = (
        "loginUrl="
        + urllib.parse.quote(login_url)
        + "&loginRequestData="
        + urllib.parse.quote(login_request_data)
    )
    zap.authentication.set_authentication_method(
        context_id, "formBasedAuthentication", form_based_config
    )

    user = "admin"
    user_id = zap.users.new_user(context_id, user)
    user_auth_config = (
        "username="
        + urllib.parse.quote(username)
        + "&password="
        + urllib.parse.quote(password)
    )

    zap.users.set_authentication_credentials(context_id, user_id, user_auth_config)
    zap.users.set_user_enabled(context_id, user_id, "true")
    zap.forcedUser.set_forced_user(context_id, user_id)

    print("\n\n\n\n\n\n")
    print(zap.forcedUser.set_forced_user_mode_enabled(True))

    zap.spider.scan_as_user(context_id, user_id, target, recurse="true")
    zap.ajaxSpider.scan_as_user(context_name, "admin", target)

    print("\n\n\n\n\n\n")
    print(zap.ascan.set_option_handle_anti_csrf_tokens(True))
    # print(zap.ascan.scan_as_user(target, context_id, user_id, recurse=True))
