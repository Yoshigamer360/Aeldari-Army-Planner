# Aeldari Army Planner by YoshiGamer360
# Project began on 22/06/24

import os, random

armyCharacterList = []
armyBattlelineList = []
armyTransportList = []
armyOtherList = []
armyEnhanceList = []
armyCharacterPoints, armyBattlelinePoints, armyTransportPoints = 0, 0, 0
armyOtherPoints, armyEnhancePoints = 0, 0
maxArmyPoints, fullArmyPoints = 1000, 0

def menu():
  global armyCharacterList
  global armyBattlelineList
  global armyTransportList
  global armyOtherList
  global armyEnhanceList
  global armyCharacterPoints
  global armyBattlelinePoints
  global armyTransportPoints
  global armyOtherPoints
  global armyEnhancePoints
  global fullArmyPoints
  global maxArmyPoints
  os.system("clear")
  print("If you would like to see the character list enter: A \n")
  print("If you would like to see the battleline list enter: B \n")
  print("If you would like to see the transport list enter: C \n")
  print("If you would like to see the other datasheets list enter: D \n")
  print("If you would like to see the enhancement list enter: E \n")
  print("If you would like to see your army list enter: X \n")
  menuQuestions = input("Enter: ")
  if menuQuestions.lower() == "a":
    showCharacterList()
    while True:
      print('\nIf you would like to add one of these units to your army then type "add" then the corresponding number. \nIf you would like to remove one of these units then type "remove" and then the corresponding number.')
      print('If you would like to return to the menu then type "menu". DONT LEAVE ANY SPACES!')
      listQuestion = input("Type and enter here: ")
      if listQuestion.lower().startswith("add"):
        if listQuestion[3:] == "1":
          armyCharacterList.append("Asurmen")
          armyCharacterPoints += 135
        elif listQuestion[3:] == "2":
          armyCharacterList.append("Autarch")
          armyCharacterPoints += 75
        elif listQuestion[3:] == "3":
          armyCharacterList.append("Autarch Skyrunner")
          armyCharacterPoints += 90
        elif listQuestion[3:] == "4":
          armyCharacterList.append("Autarch Wayleaper")
          armyCharacterPoints += 115
        elif listQuestion[3:] == "5":
          armyCharacterList.append("Avatar of Khaine")
          armyCharacterPoints += 335
        elif listQuestion[3:] == "6":
          armyCharacterList.append("Baharroth")
          armyCharacterPoints += 125
        elif listQuestion[3:] == "7":
          armyCharacterList.append("Death Jester")
          armyCharacterPoints += 90
        elif listQuestion[3:] == "8":
          armyCharacterList.append("Eldrad Ulthran")
          armyCharacterPoints += 110
        elif listQuestion[3:] == "9":
          armyCharacterList.append("Farseer")
          armyCharacterPoints += 80
        elif listQuestion[3:] == "10":
          armyCharacterList.append("Farseer Skyrunner")
          armyCharacterPoints += 90
        elif listQuestion[3:] == "11":
          armyCharacterList.append("Fuegan")
          armyCharacterPoints += 115
        elif listQuestion[3:] == "12":
          armyCharacterList.append("Illiac Nightspear")
          armyCharacterPoints += 70
        elif listQuestion[3:] == "13":
          armyCharacterList.append("Irillyth")
          armyCharacterPoints += 105
        elif listQuestion[3:] == "14":
          armyCharacterList.append("Jain Zar")
          armyCharacterPoints += 105
        elif listQuestion[3:] == "15":
          armyCharacterList.append("Karandras")
          armyCharacterPoints += 100
        elif listQuestion[3:] == "16":
          armyCharacterList.append("Maugan Ra")
          armyCharacterPoints += 130
        elif listQuestion[3:] == "17":
          armyCharacterList.append("Prince Yriel")
          armyCharacterPoints += 100
        elif listQuestion[3:] == "18":
          armyCharacterList.append("Shadowseer")
          armyCharacterPoints += 60
        elif listQuestion[3:] == "19":
          armyCharacterList.append("Solitaire")
          armyCharacterPoints += 115
        elif listQuestion[3:] == "20":
          armyCharacterList.append("Spirit Seer")
          armyCharacterPoints += 65
        elif listQuestion[3:] == "21":
          armyCharacterList.append("The Visarch")
          armyCharacterPoints += 90
        elif listQuestion[3:] == "22":
          armyCharacterList.append("The Yncarne")
          armyCharacterPoints += 350
        elif listQuestion[3:] == "23":
          armyCharacterList.append("Troupe Master")
          armyCharacterPoints += 55
        elif listQuestion[3:] == "24":
          armyCharacterList.append("Warlock")
          armyCharacterPoints += 45
        elif listQuestion[3:] == "25":
          armyCharacterList.append("Warlock Skyrunner")
          armyCharacterPoints += 55
        elif listQuestion[3:] == "26":
          armyCharacterList.append("Yvraine")
          armyCharacterPoints += 100
      elif listQuestion.lower().startswith("remove"):
        if listQuestion[6:] == "1":
          armyCharacterList.remove("Asurmen")
          armyCharacterPoints -= 135
        elif listQuestion[6:] == "2":
          armyCharacterList.append("Autarch")
          armyCharacterPoints -= 75
        elif listQuestion[6:] == "3":
          armyCharacterList.remove("Autarch Skyrunner")
          armyCharacterPoints -= 90
        elif listQuestion[6:] == "4":
          armyCharacterList.remove("Autarch Wayleaper")
          armyCharacterPoints -= 115
        elif listQuestion[6:] == "5":
          armyCharacterList.remove("Avatar of Khaine")
          armyCharacterPoints -= 335
        elif listQuestion[6:] == "6":
          armyCharacterList.remove("Baharroth")
          armyCharacterPoints -= 125
        elif listQuestion[6:] == "7":
          armyCharacterList.remove("Death Jester")
          armyCharacterPoints -= 90
        elif listQuestion[6:] == "8":
          armyCharacterList.remove("Eldrad Ulthran")
          armyCharacterPoints -= 110
        elif listQuestion[6:] == "9":
          armyCharacterList.remove("Farseer")
          armyCharacterPoints -= 80
        elif listQuestion[6:] == "10":
          armyCharacterList.remove("Farseer Skyrunner")
          armyCharacterPoints -= 90
        elif listQuestion[6:] == "11":
          armyCharacterList.remove("Fuegan")
          armyCharacterPoints -= 115
        elif listQuestion[6:] == "12":
          armyCharacterList.remove("Illiac Nightspear")
          armyCharacterPoints -= 70
        elif listQuestion[6:] == "13":
          armyCharacterList.remove("Irillyth")
          armyCharacterPoints -= 105
        elif listQuestion[6:] == "14":
          armyCharacterList.remove("Jain Zar")
          armyCharacterPoints -= 105
        elif listQuestion[6:] == "15":
          armyCharacterList.remove("Karandras")
          armyCharacterPoints -= 100
        elif listQuestion[6:] == "16":
          armyCharacterList.remove("Maugan Ra")
          armyCharacterPoints -= 130
        elif listQuestion[6:] == "17":
          armyCharacterList.remove("Prince Yriel")
          armyCharacterPoints -= 100
        elif listQuestion[6:] == "18":
          armyCharacterList.remove("Shadowseer")
          armyCharacterPoints -= 60
        elif listQuestion[6:] == "19":
          armyCharacterList.remove("Solitaire")
          armyCharacterPoints -= 115
        elif listQuestion[6:] == "20":
          armyCharacterList.remove("Spirit Seer")
          armyCharacterPoints -= 65
        elif listQuestion[6:] == "21":
          armyCharacterList.remove("The Visarch")
          armyCharacterPoints -= 90
        elif listQuestion[6:] == "22":
          armyCharacterList.remove("The Yncarne")
          armyCharacterPoints -= 350
        elif listQuestion[6:] == "23":
          armyCharacterList.remove("Troupe Master")
          armyCharacterPoints -= 55
        elif listQuestion[6:] == "24":
          armyCharacterList.remove("Warlock")
          armyCharacterPoints -= 45
        elif listQuestion[6:] == "25":
          armyCharacterList.remove("Warlock Skyrunner")
          armyCharacterPoints -= 55
        elif listQuestion[6:] == "26":
          armyCharacterList.remove("Yvraine")
          armyCharacterPoints -= 100
      elif listQuestion.lower() == "menu":
        menu()
        break
      showCharacterList()
  elif menuQuestions.lower() == "b":
    showBattlelineList()
    while True:
      print('\nIf you would like to add one of these units to your army then type "add" then the corresponding number. \nIf you would like to remove one of these units then type "remove" and then the corresponding number.')
      print('If you would like to return to the menu then type "menu". DONT LEAVE ANY SPACES!')
      listQuestion = input("Type and enter here: ")
      if listQuestion.lower().startswith("add"):
        if listQuestion[3:] == "1":
          armyBattlelineList.append("Corsair Voidreavers")
          armyBattlelinePoints += 70
        elif listQuestion[3:] == "2":
          armyBattlelineList.append("Guardian Defenders")
          armyBattlelinePoints += 110
        elif listQuestion[3:] == "3":
          armyBattlelineList.append("Storm Guardians")
          armyBattlelinePoints += 115
        elif listQuestion[3:] == "4":
          armyBattlelineList.append("Troupe")
          armyBattlelinePoints += 75
      elif listQuestion.lower().startswith("remove"):
        if listQuestion[6:] == "1":
          armyBattlelineList.remove("Corsair Voidreavers")
          armyBattlelinePoints -= 70
        elif listQuestion[6:] == "2":
          armyBattlelineList.remove("Guardian Defenders")
          armyBattlelinePoints -= 110
        elif listQuestion[6:] == "3":
          armyBattlelineList.remove("Storm Guardians")
          armyBattlelinePoints -= 115
        elif listQuestion[6:] == "4":
          armyBattlelineList.remove("Troupe")
          armyBattlelinePoints -= 75
      elif listQuestion.lower() == "menu":
        menu()
        break
      showBattlelineList()
  elif menuQuestions.lower() == "c":
    showTransportList()
    while True:
      print('\nIf you would like to add one of these units to your army then type "add" then the corresponding number. \nIf you would like to remove one of these units then type "remove" and then the corresponding number.')
      print('If you would like to return to the menu then type "menu". DONT LEAVE ANY SPACES!')
      listQuestion = input("Type and enter here: ")
      if listQuestion.lower().startswith("add"):
        if listQuestion[3:] == "1":
          armyTransportList.append("Starweaver")
          armyTransportPoints += 80
        elif listQuestion[3:] == "2":
          armyTransportList.append("Wave Serpent")
          armyTransportPoints += 120
      elif listQuestion.lower().startswith("remove"):
        if listQuestion[6:] == "1":
          armyTransportList.remove("Starweaver")
          armyTransportPoints -= 80
        elif listQuestion[6:] == "2":
          armyTransportList.remove("Wave Serpent")
          armyTransportPoints -= 120
      elif listQuestion.lower() == "menu":
        menu()
        break
      showTransportList()
  elif menuQuestions.lower() == "d":
    showOthersList()
    while True:
      print('\nIf you would like to add one of these units to your army then type "add" then the corresponding number. \nIf you would like to remove one of these units then type "remove" and then the corresponding number.')
      print('If you would like to return to the menu then type "menu". DONT LEAVE ANY SPACES!')
      listQuestion = input("Type and enter here: ")
      if listQuestion.lower().startswith("add"):
        if listQuestion[3:] == "1":
          armyOtherList.append("Cobra")
          armyOtherPoints += 415
        elif listQuestion[3:] == "2":
          armyOtherList.append("Corsair Voidscarred")
          armyOtherPoints += 90
        elif listQuestion[3:] == "3":
          armyOtherList.append("Crimson Hunter")
          armyOtherPoints += 160
        elif listQuestion[3:] == "4":
          armyOtherList.append("Dark Reapers")
          armyOtherPoints += 80
        elif listQuestion[3:] == "5":
          armyOtherList.append("Dire Avengers")
          armyOtherPoints += 70
        elif listQuestion[3:] == "6":
          armyOtherList.append("Falcon")
          armyOtherPoints += 140
        elif listQuestion[3:] == "7":
          armyOtherList.append("Fire Dragons")
          armyOtherPoints += 85
        elif listQuestion[3:] == "8":
          armyOtherList.append("Fire Prism")
          armyOtherPoints += 180
        elif listQuestion[3:] == "9":
          armyOtherList.append("Hemlock Wraithfighter")
          armyOtherPoints += 155
        elif listQuestion[3:] == "10":
          armyOtherList.append("Hornet")
          armyOtherPoints += 100
        elif listQuestion[3:] == "11":
          armyOtherList.append("Howling Banshees")
          armyOtherPoints += 85
        elif listQuestion[3:] == "12":
          armyOtherList.append("Lynx")
          armyOtherPoints += 180
        elif listQuestion[3:] == "13":
          armyOtherList.append("Night Spinner")
          armyOtherPoints += 180
        elif listQuestion[3:] == "14":
          armyOtherList.append("Nightwing")
          armyOtherPoints += 150
        elif listQuestion[3:] == "15":
          armyOtherList.append("Phantom Titan")
          armyOtherPoints += 2100
        elif listQuestion[3:] == "16":
          armyOtherList.append("Rangers")
          armyOtherPoints += 55
        elif listQuestion[3:] == "17":
          armyOtherList.append("Revenant Titan")
          armyOtherPoints += 1100
        elif listQuestion[3:] == "18":
          armyOtherList.append("Scorpion")
          armyOtherPoints += 410
        elif listQuestion[3:] == "19":
          armyOtherList.append("Shadow Spectre")
          armyOtherPoints += 95
        elif listQuestion[3:] == "20":
          armyOtherList.append("Shining Spears")
          armyOtherPoints += 120
        elif listQuestion[3:] == "21":
          armyOtherList.append("Shroud Runners")
          armyOtherPoints += 80
        elif listQuestion[3:] == "22":
          armyOtherList.append("Skathach Wraithknight")
          armyOtherPoints += 490
        elif listQuestion[3:] == "23":
          armyOtherList.append("Skyweavers")
          armyOtherPoints += 95
        elif listQuestion[3:] == "24":
          armyOtherList.append("Striking Scorpions")
          armyOtherPoints += 75
        elif listQuestion[3:] == "25":
          armyOtherList.append("Support Weapons")
          armyOtherPoints += 125
        elif listQuestion[3:] == "26":
          armyOtherList.append("Swooping Hawks")
          armyOtherPoints += 75
        elif listQuestion[3:] == "27":
          armyOtherList.append("Voidweaver")
          armyOtherPoints += 125
        elif listQuestion[3:] == "28":
          armyOtherList.append("Vypers")
          armyOtherPoints += 85
        elif listQuestion[3:] == "29":
          armyOtherList.append("War Walkers")
          armyOtherPoints += 110
        elif listQuestion[3:] == "30":
          armyOtherList.append("Warlock Conclave")
          armyOtherPoints += 60
        elif listQuestion[3:] == "31":
          armyOtherList.append("Warlock Skyrunner Conclave")
          armyOtherPoints += 100
        elif listQuestion[3:] == "32":
          armyOtherList.append("Warp Hunter")
          armyOtherPoints += 145
        elif listQuestion[3:] == "33":
          armyOtherList.append("Warp Spiders")
          armyOtherPoints += 115
        elif listQuestion[3:] == "34":
          armyOtherList.append("Webway Gate")
          armyOtherPoints += 220
        elif listQuestion[3:] == "35":
          armyOtherList.append("Windriders")
          armyOtherPoints += 80
        elif listQuestion[3:] == "36":
          armyOtherList.append("Wraithblades")
          armyOtherPoints += 170
        elif listQuestion[3:] == "37":
          armyOtherList.append("Wraithguard")
          armyOtherPoints += 170
        elif listQuestion[3:] == "38":
          armyOtherList.append("Wraithknight")
          armyOtherPoints += 510
        elif listQuestion[3:] == "39":
          armyOtherList.append("Wraithlord")
          armyOtherPoints += 160
        elif listQuestion[3:] == "40":
          armyOtherList.append("Wraithseer")
          armyOtherPoints += 160
      if listQuestion.lower().startswith("remove"):
        if listQuestion[6:] == "1":
          armyOtherList.append("Cobra")
          armyOtherPoints -= 415
        elif listQuestion[6:] == "2":
          armyOtherList.append("Corsair Voidscarred")
          armyOtherPoints -= 90
        elif listQuestion[6:] == "3":
          armyOtherList.append("Crimson Hunter")
          armyOtherPoints -= 160
        elif listQuestion[6:] == "4":
          armyOtherList.append("Dark Reapers")
          armyOtherPoints -= 80
        elif listQuestion[6:] == "5":
          armyOtherList.append("Dire Avengers")
          armyOtherPoints -= 70
        elif listQuestion[6:] == "6":
          armyOtherList.append("Falcon")
          armyOtherPoints -= 140
        elif listQuestion[6:] == "7":
          armyOtherList.append("Fire Dragons")
          armyOtherPoints -= 85
        elif listQuestion[6:] == "8":
          armyOtherList.append("Fire Prism")
          armyOtherPoints -= 180
        elif listQuestion[6:] == "9":
          armyOtherList.append("Hemlock Wraithfighter")
          armyOtherPoints -= 155
        elif listQuestion[6:] == "10":
          armyOtherList.append("Hornet")
          armyOtherPoints -= 100
        elif listQuestion[6:] == "11":
          armyOtherList.append("Howling Banshees")
          armyOtherPoints -= 85
        elif listQuestion[6:] == "12":
          armyOtherList.append("Lynx")
          armyOtherPoints -= 180
        elif listQuestion[6:] == "13":
          armyOtherList.append("Night Spinner")
          armyOtherPoints -= 180
        elif listQuestion[6:] == "14":
          armyOtherList.append("Nightwing")
          armyOtherPoints -= 150
        elif listQuestion[6:] == "15":
          armyOtherList.append("Phantom Titan")
          armyOtherPoints -= 2100
        elif listQuestion[6:] == "16":
          armyOtherList.append("Rangers")
          armyOtherPoints -= 55
        elif listQuestion[6:] == "17":
          armyOtherList.append("Revenant Titan")
          armyOtherPoints -= 1100
        elif listQuestion[6:] == "18":
          armyOtherList.append("Scorpion")
          armyOtherPoints -= 410
        elif listQuestion[6:] == "19":
          armyOtherList.append("Shadow Spectre")
          armyOtherPoints -= 95
        elif listQuestion[6:] == "20":
          armyOtherList.append("Shining Spears")
          armyOtherPoints -= 120
        elif listQuestion[6:] == "21":
          armyOtherList.append("Shroud Runners")
          armyOtherPoints -= 80
        elif listQuestion[6:] == "22":
          armyOtherList.append("Skathach Wraithknight")
          armyOtherPoints -= 490
        elif listQuestion[6:] == "23":
          armyOtherList.append("Skyweavers")
          armyOtherPoints -= 95
        elif listQuestion[6:] == "24":
          armyOtherList.append("Striking Scorpions")
          armyOtherPoints -= 75
        elif listQuestion[6:] == "25":
          armyOtherList.append("Support Weapons")
          armyOtherPoints -= 125
        elif listQuestion[6:] == "26":
          armyOtherList.append("Swooping Hawks")
          armyOtherPoints -= 75
        elif listQuestion[6:] == "27":
          armyOtherList.append("Voidweaver")
          armyOtherPoints -= 125
        elif listQuestion[6:] == "28":
          armyOtherList.append("Vypers")
          armyOtherPoints -= 85
        elif listQuestion[6:] == "29":
          armyOtherList.append("War Walkers")
          armyOtherPoints -= 110
        elif listQuestion[6:] == "30":
          armyOtherList.append("Warlock Conclave")
          armyOtherPoints -= 60
        elif listQuestion[6:] == "31":
          armyOtherList.append("Warlock Skyrunner Conclave")
          armyOtherPoints -= 100
        elif listQuestion[6:] == "32":
          armyOtherList.append("Warp Hunter")
          armyOtherPoints -= 145
        elif listQuestion[6:] == "33":
          armyOtherList.append("Warp Spiders")
          armyOtherPoints -= 115
        elif listQuestion[6:] == "34":
          armyOtherList.append("Webway Gate")
          armyOtherPoints -= 220
        elif listQuestion[6:] == "35":
          armyOtherList.append("Windriders")
          armyOtherPoints -= 80
        elif listQuestion[6:] == "36":
          armyOtherList.append("Wraithblades")
          armyOtherPoints -= 170
        elif listQuestion[6:] == "37":
          armyOtherList.append("Wraithguard")
          armyOtherPoints -= 170
        elif listQuestion[6:] == "38":
          armyOtherList.append("Wraithknight")
          armyOtherPoints -= 510
        elif listQuestion[6:] == "39":
          armyOtherList.append("Wraithlord")
          armyOtherPoints -= 160
        elif listQuestion[6:] == "40":
          armyOtherList.append("Wraithseer")
          armyOtherPoints -= 160
      elif listQuestion.lower() == "menu":
        menu()
        break
      showOthersList()
  elif menuQuestions.lower() == "e":
    showEnhanceList()
    while True:
      print('\nIf you would like to add one of these units to your army then type "add" then the corresponding number. \nIf you would like to remove one of these units then type "remove" and then the corresponding number.')
      print('If you would like to return to the menu then type "menu". DONT LEAVE ANY SPACES!')
      listQuestion = input("Type and enter here: ")
      if listQuestion.lower().startswith("add"):
        if listQuestion[3:] == "1":
          armyEnhanceList.append("Fates Messanger")
          armyEnhancePoints += 15
        elif listQuestion[3:] == "2":
          armyEnhanceList.append("Reader Of The Runes")
          armyEnhancePoints += 20
        elif listQuestion[3:] == "3":
          armyEnhanceList.append("The Phoenix Gem")
          armyEnhancePoints += 25        
        elif listQuestion[3:] == "4":
            armyEnhanceList.append("The Weeping Stones")
            armyEnhancePoints += 15
      elif listQuestion.lower().startswith("remove"):
        if listQuestion[3:] == "1":
          armyEnhanceList.remove("Fates Messanger")
          armyEnhancePoints -= 15
        elif listQuestion[3:] == "2":
          armyEnhanceList.remove("Reader Of The Runes")
          armyEnhancePoints += 20
        elif listQuestion[3:] == "3":
          armyEnhanceList.remove("The Phoenix Gem")
          armyEnhancePoints -= 25        
        elif listQuestion[3:] == "4":
            armyEnhanceList.remove("The Weeping Stones")
            armyEnhancePoints -= 15
      elif listQuestion.lower() == "menu":
        menu()
        break
      showEnhanceList()
  elif menuQuestions.lower() == "x":
    os.system("clear")
    armyCharacterList = list(armyCharacterList)
    armyCharacterList.sort()
    armyBattlelineList = list(armyBattlelineList)
    armyBattlelineList.sort()
    armyTransportList = list(armyTransportList)
    armyTransportList.sort()
    armyOtherList = list(armyOtherList)
    armyOtherList.sort()
    armyEnhanceList = list(armyEnhanceList)
    armyEnhanceList.sort()
    print(f"ARMY LIST: CHARACTERS (Worth {armyCharacterPoints} pts)\n")
    for character in armyCharacterList:
      print(character)
    print(f"\nARMY LIST: BATTLELINE (Worth {armyBattlelinePoints} pts) \n")
    for battleline in armyBattlelineList:
      print(battleline)
    print(f"\nARMY LIST: DEDICATED TRANSPORT (Worth {armyTransportPoints} pts) \n")
    for transport in armyTransportList:
      print(transport)
    print(f"\nARMY LIST: OTHER DATASHEETS (Worth {armyOtherPoints} pts) \n")
    for other in armyOtherList:
      print(other)
    print(f"\nARMY LIST: ENHANCEMENTS DATASHEETS (Worth {armyEnhancePoints} pts) \n")
    for enhance in armyEnhanceList:
      print(enhance)
    fullArmyPoints = armyCharacterPoints + armyBattlelinePoints + armyTransportPoints + armyOtherPoints + armyEnhancePoints
    print(f"\nTOTAL ARMY POINTS = {fullArmyPoints} / {maxArmyPoints}\n")

  else:
    menu()
  input("Press enter to return to the menu.")


def showCharacterList():
  os.system("clear")
  print("Here is a list of Aeldari characters \n")
  print("1) Asurmen = 135")
  print("2) Autarch = 75")
  print("3) Autarch Skyrunner = 90")
  print("4) Autarch Wayleaper = 115")
  print("5) Avatar of Khaine = 335")
  print("6) Baharroth = 125")
  print("7) Death Jester = 90")
  print("8) Eldrad Ulthran = 110")
  print("9) Farseer = 80")
  print("10) Farseer Skyrunner = 90")
  print("11) Fuegan = 115")
  print("12) Illiac Nightspear = 70")
  print("13) Irillyth = 105")
  print("14) Jain Zar = 105")
  print("15) Karandras = 100")
  print("16) Maugan Ra = 130")
  print("17) Prince Yriel = 100")
  print("18) Shadowseer = 60")
  print("19) Solitaire = 115")
  print("20) Spirit Seer = 65")
  print("21) The Visarch = 90")
  print("22) The Yncarne = 350")
  print("23) Troupe Master = 55")
  print("24) Warlock = 45")
  print("25) Warlock Skyrunner = 55")
  print("26) Yvraine = 100")
  print()

def showBattlelineList():
  os.system("clear")
  print("Here is a list of Aeldari battleline troops \n")
  print("1) Corsair Voidreavers = 70")
  print("2) Guardian Defenders = 110")
  print("3) Storm Guardians = 115")
  print("4) Troupe = 75")

def showTransportList():
  os.system("clear")
  print("Here is a list of Aeldari dedicated transports \n")
  print("1) Starweaver = 80")
  print("2) Wave Serpent = 120")

def showOthersList():
  os.system("clear")
  print("Here is a list of other Aeldari datasheets \n")
  print("1) Cobra = 415")
  print("2) Corsair Voidscarred = 90")
  print("3) Crimson Hunter = 160")
  print("4) Dark Reapers = 80")
  print("5) Dire Avengers = 70")
  print("6) Falcon = 140")
  print("7) Fire Dragons = 85")
  print("8) Fire Prism = 180")
  print("9) Hemlock Wraithfighter = 155")
  print("10) Hornet = 100")
  print("11) Howling Banshees = 85")
  print("12) Lynx = 180")
  print("13) Night Spinner = 180")
  print("14) Nightwing = 150")
  print("15) Phantom Titan = 2100")
  print("16) Rangers = 55")
  print("17) Revenant Titan = 1100")
  print("18) Scorpion = 410")
  print("19) Shadow Spectres = 95")
  print("20) Shining Spears = 120")
  print("21) Shroud Runners = 80")
  print("22) Skathach Wraithknight = 490")
  print("23) Skyweavers = 95")
  print("24) Striking Scorpions = 75")
  print("25) Support Weapons = 125")
  print("26) Swooping Hawks = 75")
  print("27) Voidweaver = 125")
  print("28) Vypers = 85")
  print("29) War Walkers = 110")
  print("30) Warlock Conclave = 60")
  print("31) Warlock Skyrunner Conlave = 100")
  print("32) Warp Hunter = 145")
  print("33) Warp Spiders = 115")
  print("34) Webway Gate = 220")
  print("35) Windriders = 80")
  print("36) Wraithblades = 170")
  print("37) Wraithguard = 170")
  print("38) Wraithknight = 510")
  print("39) Wraithlord = 160")
  print("40) Wraithseer = 160")

def showEnhanceList():
  os.system("clear")
  print("Here is a list of Aeldari enhancements \n")
  print("1) Fates Messanger = 15")
  print("2) Reader Of The Runes = 20")
  print("3) The Phoenix Gem = 25")
  print("4) The Weeping Stones = 15")

print("Welcome to the Aeldari Army Planner where you can see what characters add up to without using another army roster.\n")
os.system("clear")
print("You have chosen to create a new army\n")
print("A) Incursion 1000 points, B) Strikeforce 2000 points, C) Onslaught 3000 points")
armySize = input("Enter the corresponding letter for your army size: ")
if armySize.lower() == "a":
  maxArmyPoints = "1000"
elif armySize.lower() == "b":
  maxPoints = "2000"
elif armySize.lower() == "c":
  maxArmyPoints = "3000"
while True:
  menu()
