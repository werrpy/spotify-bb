# spotify-bb
Spotify BBCode formatter

Requirements  
Python 2 or 3
```
pip install spotipy
```

Usage
```
python spotifybb.py spotifyid
```

Sample Output
```
> python spotifybb.py 5dj2UjtSxuKGlb17Bzu1mL
Label: Glassnote Entertainment Group LLC
Name: Love Is Dead
Release Date: 2018-05-25
URLs:
spotify: [url=https://open.spotify.com/album/5dj2UjtSxuKGlb17Bzu1mL]https://open.spotify.com/album/5dj2UjtSxuKGlb17Bzu1mL[/url]
Images:
640x640 [center][img]https://i.scdn.co/image/159e339c6cd980e4787e7d464079d822b19425be[/img][/center]
300x300 [center][img]https://i.scdn.co/image/7757d5799cf45c08c2a84f6ed942399080ea16d8[/img][/center]
64x64   [center][img]https://i.scdn.co/image/ea4bb5007473a22fbdcaeac7aea037b25ebedd2b[/img][/center]
Tracks:
[list=1][*]1 Graffiti 03:38[/*][*]2 Get Out 03:51[/*][*]3 Deliverance 04:12[/*][*]4 My Enemy 03:53[/*][*]5 Forever 03:44[/*][*]6 Never Say Die 04:23[/*][*]7 Miracle 03:08[/*][*]8 Graves 04:43[/*][*]9 Heaven/Hell 05:05[/*][*]10 God's Plan 03:31[/*][*]11 Really Gone 03:11[/*][*]12 ii 01:09[/*][*]13 Wonderland 04:35[/*][/list]
```

### Spotify API

Create a client id at https://developer.spotify.com/dashboard/applications. Replace `client_id` and `client_secret` here: https://github.com/werrpy/spotify-bb/blob/master/spotifybb.py#L37-L39
