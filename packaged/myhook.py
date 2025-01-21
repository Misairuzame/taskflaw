from zapv2 import ZAPv2


def zap_started(zap: ZAPv2, target):
    print("myhook.py: The target is:", target)

    zap.replacer.add_rule(
        description="Remove 'complete=on' from POST data",
        enabled=True,
        matchtype="REQ_BODY_STR",
        matchregex=False,
        matchstring="&complete=on",
        replacement="",
    )

    # print(zap.ascan.scanners())
    # print("\n\n\n\n")

    # Disabilita User Agent Fuzzer
    zap.ascan.disable_scanners("10104")


def zap_pre_shutdown(zap):
    print("myhook.py: Printing stats before shutdown...")
    print(zap.stats.site_stats("http://172.17.0.1:8000", "stats.auth"))
