# coding: utf-8

from enum import Enum
from six import string_types
from bitmovin_api_sdk.common.poscheck import poscheck_model


class InputStreamType(Enum):
    INGEST = "INGEST"
    CONCATENATION = "CONCATENATION"
    TRIMMING_TIME_BASED = "TRIMMING_TIME_BASED"
    TRIMMING_TIME_CODE_TRACK = "TRIMMING_TIME_CODE_TRACK"
    TRIMMING_H264_PICTURE_TIMING = "TRIMMING_H264_PICTURE_TIMING"
    AUDIO_MIX = "AUDIO_MIX"
    FILE = "FILE"