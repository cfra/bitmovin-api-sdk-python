# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_impression_details import AnalyticsImpressionDetails
from bitmovin_api_sdk.models.analytics_license import AnalyticsLicense
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class ImpressionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ImpressionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, impression_id, analytics_license, **kwargs):
        # type: (string_types, AnalyticsLicense, dict) -> AnalyticsImpressionDetails
        """Impression Details

        :param impression_id: Impression id
        :type impression_id: string_types, required
        :param analytics_license: Analytics license
        :type analytics_license: AnalyticsLicense, required
        :return: Service specific result
        :rtype: AnalyticsImpressionDetails
        """

        return self.api_client.post(
            '/analytics/impressions/{impression_id}',
            analytics_license,
            path_params={'impression_id': impression_id},
            type=AnalyticsImpressionDetails,
            **kwargs
        )