from museum.artwork import get_artworks
from museum.artists import get_artists
def main():
  artwork = input("Artwork: ")
  artworks = get_artworks(artwork,limit=3)
  for artwork in artworks:
    print(f"*{artwork}")
  artist = input("Artist: ")
  artists = get_artists(artist, limit=3)
  for artist in artists:
    print(f"*{artist}")

main()
