import sys
def main():
  coordinates_tuple = (42.376, -71.115)
  coordinates_lists = [42.376, -71.115]
  
  latitude, longitude = coordinates_tuple
  print(f"Latitude: {latitude}")
  print(f"Longitude: {longitude}")
  print(f"{sys.getsizeof(coordinates_tuple)} bytes")
  print(f"{sys.getsizeof(coordinates_lists)} bytes")
  

main()  