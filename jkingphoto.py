import requests
# 1670994053197921
# https://graph.facebook.com/1670994053197921/feed
# TODO: Automate to post daily.
# TODO: Sun Tzu quotes
# Dependencies: python requests
# Maintenance: Replace acccess token every 60 days
r = requests.post('https://graph.facebook.com/1670994053197921/photos', data={'url': 'https://i.imgur.com/vRivhPX.jpg',
'caption': 'mr king funny haha pt. 2',
'access_token': 'EABjkwuSyAgEBALZBOnYybSAdsL4ZA5LA2OriZC5QcQt3eROBJ0h7Dt88R8rCm2JVZCZCaaekdMmZBDE97zWZAq7b3dxzk0lXb8lMxxJcdqGWCsDAV6PVQIsLOhTraCBgMZBptpIUt0g5G3UswJwY22GTrpVu3XVv9h4ycxRKTK0uCOBZAlF24pMlm'})