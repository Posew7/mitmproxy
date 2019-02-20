import mitmproxy

def request(flow):
    print("istekler bastırılıyor")
    print(flow)

def response(flow):
    print("cevaplar bastırılıyor")
    print(flow)