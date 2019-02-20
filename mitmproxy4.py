import mitmproxy

def request(flow):
    if (flow.request.pretty_url.endswith(".exe")):
        print("\n\nBURADA BİR EXE DOSYASI YAKALANDI\n\n")
        print(flow.request.pretty_url)