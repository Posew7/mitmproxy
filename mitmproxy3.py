import mitmproxy

def request(flow):
    print(flow.request.pretty_url)