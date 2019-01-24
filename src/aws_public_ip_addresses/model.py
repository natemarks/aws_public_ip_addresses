class AWSAddresses(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    """
    json_download_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'  # type: str

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = {}
        self.kwargs.update(kwargs)

    @classmethod
    def get_address_data(cls):
        import urllib2
        import json

        json_data = urllib2.urlopen(AWSAddresses.json_download_url).read()

        return json.loads(json_data)
