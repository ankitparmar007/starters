def getTime(my_time):

  hours = int(my_time) // 60

  # Get additional minutes with modulus
  minutes = int(my_time) % 60

  # Create time as a string
  time_string = f"{hours}h {minutes}m"
  
  return time_string
