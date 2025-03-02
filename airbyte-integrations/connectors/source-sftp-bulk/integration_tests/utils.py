# Copyright (c) 2024 Airbyte, Inc., all rights reserved.


import json
import logging
import os
import re
from typing import Any, Mapping, Union


logger = logging.getLogger("airbyte")

TMP_FOLDER = "/tmp/test_sftp_source"


def load_config(config_path: str) -> Mapping[str, Any]:
    with open(f"{os.path.dirname(__file__)}/configs/{config_path}", "r") as config:
        return json.load(config)


def write_config(config_path: str, config: Mapping[str, Any]):
    with open(f"{os.path.dirname(__file__)}/configs/{config_path}", "w") as config_file:
        config = json.dumps(config)
        config_file.write(config)


def get_docker_ip() -> Union[str, Any]:
    # When talking to the Docker daemon via a UNIX socket, route all TCP
    # traffic to docker containers via the TCP loopback interface.
    docker_host = os.environ.get("DOCKER_HOST", "").strip()
    if not docker_host or docker_host.startswith("unix://"):
        return "127.0.0.1"

    match = re.match(r"^tcp://(.+?):\d+$", docker_host)
    if not match:
        raise ValueError('Invalid value for DOCKER_HOST: "%s".' % (docker_host,))
    return match.group(1)
