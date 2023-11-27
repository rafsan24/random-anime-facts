from dragon import Dragon
from pirate import Pirate
from titan import Titan
from hunter import Hunter
from demon import Demon

def main():
  db_facts = Dragon()
  op_facts = Pirate()
  aot_facts = Titan()
  hxh_facts = Hunter()
  ds_facts = Demon()
  
  user_input = input("Would you like to learn a random fact about the anime... \n(1) 'One Piece' \n(2) 'Dragon Ball' \n(3) 'Attack on Titan' \n(4) 'Hunter x Hunter' \n(5) 'Demon Slayer' \nPlease enter '1', '2', '3', '4', or '5': ")

  try:
    user_input = int(user_input)
    if user_input < 1 or user_input > 5:
      print("Please choose from the list")
      exit()
  except:
    print("Please try again")
    exit()

  if user_input == 1:
    op_facts.get()
    print(op_facts)
  elif user_input == 2:
    db_facts.get()
    print(db_facts)
  elif user_input == 3:
    aot_facts.get()
    print(aot_facts)
  elif user_input == 4:
    hxh_facts.get()
    print(hxh_facts)
  elif user_input == 5:
    ds_facts.get()
    print(ds_facts)
    
main()
