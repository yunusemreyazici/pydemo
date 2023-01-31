import urllib.request

while True:
    with urllib.request.urlopen('https://profile-counter.glitch.me/{mucahitAgdin}/count.svg') as f:
        html = f.read().decode('utf-8')
    