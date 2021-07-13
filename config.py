#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "0fb8ae5b-66e0-418f-b786-3cc2cf89f5cc")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "1FfD34osl~9LR_Zs~H_lBT8rLfdseOXu93")
    CONNECTION_NAME = os.environ.get("ConnectionName", "aadv2")
