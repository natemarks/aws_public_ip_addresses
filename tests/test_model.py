from aws_public_ip_addresses.model import AWSAddresses


def test_check_download():
    """
    We expect the 'prefixes' key to exist at the top of the json download object
    """
    assert 'prefixes' in AWSAddresses.download_and_get_data()


def test_get_data():
    addresses = AWSAddresses()
    output = addresses.get_data()
    assert 'prefixes' in output


def test_get_ipv4_prefixes():
    addresses = AWSAddresses()
    assert len(addresses.get_ipv4_prefixes()) > 0


def test_get_ipv6_prefixes():
    addresses = AWSAddresses()
    assert len(addresses.get_ipv6_prefixes()) > 0


def test_get_regions():
    """
    :return:
    """
    addresses = AWSAddresses()

    all_regions = ['GLOBAL', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-southeast-1',
                   'ap-southeast-2', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-north-1',
                   'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2',
                   'us-gov-east-1', 'us-gov-west-1', 'us-west-1', 'us-west-2']

    all_regions.sort()

    ipv4_regions = ['GLOBAL', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-southeast-1',
                    'ap-southeast-2', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-north-1',
                    'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2',
                    'us-gov-east-1', 'us-gov-west-1', 'us-west-1', 'us-west-2']

    ipv4_regions.sort()

    ipv6_regions = ['GLOBAL', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-southeast-1',
                    'ap-southeast-2', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-north-1',
                    'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2',
                    'us-gov-east-1', 'us-gov-west-1', 'us-west-1', 'us-west-2']

    ipv6_regions.sort()

    assert all_regions == addresses.get_regions()
    assert ipv4_regions == addresses.get_regions(ip_version=4)
    assert ipv6_regions == addresses.get_regions(ip_version=6)


def test_filter_ipv4_prefixes():
    addresses = AWSAddresses()
    assert len(addresses.filter_ipv4_prefixes('us-east-')) > 0


def test_filter_ipv6_prefixes():
    addresses = AWSAddresses()
    assert len(addresses.filter_ipv6_prefixes('us-east-')) > 0
