import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import argparse

class BBCode:
  def link(self, url):
    return '[url=' + str(url) + ']' + str(url) + '[/url]'

  def image(self, url):
    return '[center][img]' + str(url) + '[/img][/center]'
    
  def tracklist(self, list):
    bbcode = '[list=1]'
    for track in list:
      if not 'track_number' in track and not 'name' in track and not 'duration_ms' in track:
        break
      bbcode += '[*]'
      if 'track_number' in track:
        bbcode += str(track['track_number'])
      if 'name' in track:
        bbcode += ' ' + track['name']
      if 'duration_ms' in track:
        millis = int(track['duration_ms'])
        seconds = str(int((millis / 1000) % 60))
        minutes = str(int((millis / (1000 * 60)) % 60))
        hours = int((millis/(1000 * 60 * 60)) % 24)

        duration = ''
        if hours is not 0:
          duration += str(hours) + ':'
        duration = '{0}{1}:{2}'.format(duration, minutes.zfill(2), seconds.zfill(2))

      bbcode += ' ' + duration + '[/*]'
    bbcode += '[/list]'
    return bbcode

# https://developer.spotify.com/dashboard/applications
client_id = '1da5c5eb87144ca3a8afeca6a9d9b7cb'
client_secret = 'caee448f0fbb48188d5909ede63250e7'

# Authenticate
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Parse arguments
parser = argparse.ArgumentParser(description='Spotify API')
parser.add_argument('spotify', type=str, help='Spotify Album ID')
args = parser.parse_args()

# CHVRCHES - Love Is Dead Album
# https://open.spotify.com/album/5dj2UjtSxuKGlb17Bzu1mL
# Spotify Album ID = args.spotify
results = sp.album(args.spotify)

# BBCode formatter
bb = BBCode()

print('Label: ' + results['label'])
print('Name: ' + results['name'])
print('Release Date: ' + results['release_date'])

print('Images: ')
for img in results['images']:
  print(str(img['height']) + 'x' + str(img['width']) + '\t' + bb.image(img['url']))

print('Tracks:')
print(bb.tracklist(results['tracks']['items']))

# Spotify urls
for k, v in results['external_urls'].items():
  print(k.capitalize() + ': ' + bb.link(v))
