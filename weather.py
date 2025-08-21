# Dress up according to weather
print("Enter the temperature outside in Degree Celsius: ")
temp = input()
if temp < 0:
  print("Wear thermals , warm swaeters, hats, hoodies,puffy jackets,socks and boots.It's really cold..brrrr")
  
elif temp < 10:
  print("Wear long swaeters, long tees, jackets, hoodies and hat")
elif temp <20:  
  print("Wear long sleeves, pants, shoes and socks and light jacket")
elif temp >20:
  print("Wear shorts ,tees, sunglasses and a hat.")
