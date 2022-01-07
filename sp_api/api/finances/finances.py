from sp_api.base import Client, Marketplaces, ApiResponse
from sp_api.base import sp_endpoint, fill_query_params


class Finances(Client):

    @sp_endpoint('/finances/v0/orders/{}/financialEvents')
    def get_financial_events_for_order(self, order_id, **kwargs):
        """
        get_financial_events_for_order(self, order_id, **kwargs)

        Examples:
            literal blocks::

                Finances().get_financial_events_for_order('485-734-5434857', MaxResultsPerPage=10)

        Args:
            order_id:
            **kwargs:

        Returns:

        """
        return self._request(fill_query_params(kwargs.pop('path'), order_id), dict(kwargs))

    @sp_endpoint('/finances/v0/financialEvents')
    def list_financial_events(self, **kwargs):
        """
        list_financial_events(self, **kwargs):


        Args:
            **kwargs:

        Returns:

        """
        return self._request(fill_query_params(kwargs.pop('path')), dict(kwargs))

    @sp_endpoint('/finances/v0/financialEventGroups/{}/financialEvents')
    def list_financial_events_by_group_id(self, event_group_id,  **kwargs):
        """
        list_financial_events_by_groupid(self, event_group_id,  **kwargs):


        Args:
            event_group_id
            **kwargs:

        Returns:

        """
        return self._request(fill_query_params(kwargs.pop('path'), event_group_id), dict(kwargs))

    @sp_endpoint('/finances/v0/financialEventGroups')
    def list_financial_event_groups(self, **kwargs):
        """
        list_financial_event_groups(self, **kwargs):


        Args:
            **kwargs:

        Returns:

        """
        return self._request(kwargs.pop('path'), dict(kwargs))

