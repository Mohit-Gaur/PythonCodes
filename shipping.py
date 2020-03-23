def ship_cost_ground(weight):
  if weight <= 2:
    price_per_round = 1.50
  elif weight <= 6:
    price_per_round = 3.00
  elif weight <= 10:
    price_per_round = 4.00
  else: 
   price_per_round = 4.75
  return 20 + (price_per_round * weight)

print(ship_cost_ground(8.4))

ship_prem_ground = 125.00

def ship_cost_drone(weight):
  if weight <= 2:
    price_per_round = 4.50
  elif weight <= 6:
    price_per_round = 9.00
  elif weight <= 10:
    price_per_round = 12.00
  else: 
   price_per_round = 14.75
  return price_per_round * weight
print(ship_cost_drone(1.5))

def cheap_ship_method(weight):
  ground = ship_cost_ground(weight)
  premium = ship_prem_ground
  drone = ship_cost_drone(weight)

  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone

  print("The cheapest option available is $%.2f with %s shipping."
  %(cost, method))

print(cheap_ship_method(4.8))
print(cheap_ship_method(41.5))
