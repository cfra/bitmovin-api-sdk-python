# coding: utf-8

from enum import Enum
from six import string_types
from bitmovin_api_sdk.common.poscheck import poscheck_model


class ManifestType(Enum):
    DASH = "DASH"
    HLS = "HLS"
    SMOOTH_STREAMING = "SMOOTH_STREAMING"