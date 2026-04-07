def main():
  spacecraft = {"name" : "Pioneer 11"}
  print(create_report(spacecraft))
  
def create_report(spacecraft):
  return f"""
  ============== Report =================
  Name: {spacecraft.get("name", "Unknown")}
  Distance: {spacecraft.get("distance", "Unknown")} AU
  ======================================
  """
  
main()