import os
import yaml
import tushare as ts

INIT = False


def init_tushare():
    global INIT
    if INIT:
        return
    p = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.env.yaml"))
    with open(p, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
        token = config["tushare_token"]
        ts.set_token(token)
        print("Tushare initialized with provided token.")
    INIT = True
