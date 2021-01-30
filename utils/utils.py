import os
import json


def read_secret_key(secret_path):
    with open(secret_path, "r") as f:
        key_id, secret_key = [x.strip() for x in f.readlines()]
    return key_id, secret_key