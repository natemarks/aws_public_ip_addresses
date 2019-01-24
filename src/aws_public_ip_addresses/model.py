from typing import List, Dict, Any


class AWSAddresses(object):
    """AWS Public IP Addresses

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    """
    json_download_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'  # type: str
    ipv4_prefix_key = 'prefixes'  # type: str
    ipv6_prefix_key = 'ipv6_prefixes'  # type: str

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = {}
        self.kwargs.update(kwargs)
        self._regions = None  # type: List[str]
        self._download_data = None
        self._ipv4_prefixes = None  # type: List[Dict[str, str]]
        self._ipv6_prefixes = None  # type: List[Dict[str, str]]

    @classmethod
    def download_and_get_data(cls) -> Dict[str, Any]:
        """Force download and return the json as nested dict

        """
        from urllib.request import urlopen
        import json

        json_data = urlopen(AWSAddresses.json_download_url).read()

        return json.loads(json_data)

    def get_data(self):
        if not self._download_data:
            self._download_data = AWSAddresses.download_and_get_data()
        return self._download_data

    def get_ipv4_prefixes(self) -> List[Dict[str, str]]:
        """The summary line for a method docstring should fit on one line.

        returns the ipv4 prefixes dict
        """
        if not self._ipv4_prefixes:
            self._ipv4_prefixes = self.get_data()[AWSAddresses.ipv4_prefix_key]
        return self._ipv4_prefixes

    def get_ipv6_prefixes(self) -> List[Dict[str, str]]:
        """The summary line for a method docstring should fit on one line.

        returns the ipv6 prefixes dict
        """
        if not self._ipv6_prefixes:
            self._ipv6_prefixes = self.get_data()[AWSAddresses.ipv6_prefix_key]
        return self._ipv6_prefixes

    def get_regions(self, ip_version: int = None) -> List[str]:
        """Return a list of the regions

        if ip_version is left default (None), the method will return a list of all unique reqions from both the ipv4
        and ipv6 prefix dicts,  If ipversion=4 is specified, it will just use the ipv4 prefix dict and if ipversion=6
        is specified it'll just use the ipv6 dict

        """
        if not self._regions:
            region_list = []
            if ip_version in [4, None]:
                for prefix in self.get_ipv4_prefixes():
                    if prefix['region'] not in region_list:
                        region_list.append(prefix['region'])

            if ip_version in [6, None]:
                for prefix in self.get_ipv6_prefixes():
                    if prefix['region'] not in region_list:
                        region_list.append(prefix['region'])

            region_list.sort()
            self._regions = region_list

        return self._regions



