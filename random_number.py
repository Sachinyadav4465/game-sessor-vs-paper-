import random
l=["rock","paper","sessor"]
 
#  rock vs paper- paper Win
# sessor vs rock - rocks win
# paper vs sessor - sessor win


while True:
    Ccount=0
    Ucount=0
    Uc=int(input(''' game start....
                         1.start
                         2.no/ exite  

'''))
    if Uc==1:
        for a in range(1,6):
          UserInput=int(input("""
                        1.rock
                        2.sessor
                        3.paper
 """))
          if UserInput==1:
             Uchoice="rock"
          elif UserInput==2:
             Uchoice="sessor"
          elif UserInput==3:
             Uchoice="paper"
          Cchoice=random.choice(l)
          print(Uchoice)
          print(Cchoice)
          if Uchoice==Cchoice:
             print("computer value",Cchoice)
             print("user value",Uchoice)
             print("game draw")
             Ucount=Ucount+1
             Ccount=Ccount+1
          elif Uchoice=="rock" and Cchoice=="paper"  or Uchoice=="sessor" and Cchoice=="rock" or Uchoice=="sessor" and Cchoice=="paper":
            print("you win")
            print("computer value",Cchoice)
            print("user value",Uchoice)
            Ucount=Ucount+1
          else:
            print("computer value",Cchoice)
            print("user value",Uchoice)
            print("computer win")
            Ccount=Ccount+1
            if Ucount==Ccount:
               print("game drwan....")
               print("computer value",Ccount)
               print("user vale",Ucount)
            elif Ucount>Ccount:
               print("you win....")
               print("computer value",Ccount)
               print("user vale",Ucount)
            else: 
              
               print("computer win....")
               print("computer value",Ccount)
               print("user vale",Ucount)
        else:
           break
        
