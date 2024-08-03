from requests import get

websites = (
    "https://google.com",
    "airbnb.com",
    "twitter.com",
    "https://faceboock.com"
)

for x in websites:
    # x.startswith('https://') === False
    if not (x.startswith('https://')): 
        x = f"https//{x}"
    print(x)

"""
https://google.com
https//airbnb.com
https//twitter.com
https://faceboock.com
"""