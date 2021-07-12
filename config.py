#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "aca1bf02-3e38-4029-b9eb-671dd37619fb")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "5pXlTj1hT1m_~N91CE0hiDJ0J2_Ui0rG-A")
    CONNECTION_NAME = os.environ.get("ConnectionName", "aadv2")
