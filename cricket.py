# [4] Python project on cricket..
import random        #Random module used to get the random runs like 1,2,3,4,6,out...
import time          # It makes the program execution to pause for certain time. Helped to design Big Toss prited and many other places.
print("\n")
print("                                 W E L C O M E  ")
print("\n")
time.sleep(1)
print("                                    TO THE   ")              #  Welcome message
print("\n")
time.sleep(1)
print("                        F A N T A S Y  C R I C K E T   W O R L D ")
print("\n")
time.sleep(1)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")
print("A Special Note:  If you want to close the program in between of the match ,\n Just press ( ctrl + c ) | But It won't work in case of selecting MODE PLAY and while taking REVIEW.")

player_on_batting=0    #All Players are in the list,it shows the index of the player in list.It increses one by one as player gets out so that next index player form the list comes to bat.
def team_selection():     # Function to select Teams,Which two team will play the match.
    global pahla_team,dusra_team,first_team_name,second_team_name,pos
    #-------------------------------------International Teams
    india = ["Rohit Sharma","Shikhar Dhawan","virat Kohli (Caption) ","KL Rahul","Hardik Pandya"]
    australia = ["David Warner","Aaron Finch (Caption) ","Glenn Maxwell","Mitchell Starc","Alex Carey"]
    england = ["Ben Stokes","Joe Root (Caption) ","Eoin Morgan","Jos Buttler","Jonny Bairstow"]
    south_africa = ["Quinton de Kock","Du Plessis (Caption) ","David Miller","Aiden Markram","JP Duminy"]
    west_indies = ["Chris Gayle","Nicholas Pooran","Shimron Hetmyer","Darren Bravo","Jason Holder (Caption) "]
    new_zealand = ["Kane Williamson (Caption) ","Martin Guptill","Ross Taylor","Henry Nicholls","Colin Munro"]
    sri_lanka = ["Dinesh Chandimal","Shehan Jayasuriya","Kusal Perera","Dimuth Karunaratne (Caption) ","Kusal Mendis"]
    bangladesh = ["Mohammad Saifuddin","Soumya Sarkar","Mosaddek Hossaain","Sabir Rahman","Shakib Al Hasan (Caption) "]
    # --------------------------------------Best Teams of Patna
    sipara_swingers = ["Rahul Kumar (Caption) ","Madhavendra Jha","Aman Kumar","Shubham Bhardwaj","Harsh Kumar"]
    beur_hitters = ["OM Shankar","Niteesh Kumar","Sachin Kumar","Faraz Ali Ahmad (Caption) ","Sumit Kumar"]
    khajanchi_avengers = ["Vicky Kumar (Caption) ","Mickey Manohar","Rajat Kumar","Abhijeet Kumar","Amardeep kumar"]
    saguna_smashers = ["Vijay kumar","Avinash Kumar (Caption) ","Aman Raj","Abhishekh Kumar","Rajnish kumar"]
    #---------------------------------------Best Teams of India
    chalukya_chargers = ["Amresh Kumar (Caption) ","Shahil Baig","Karan kumar","Abhinav Kumar","Kuldeep Chaudhari"]
    gajapathi_panthers = ["Ankit Patyal (Caption) ","Amitesh Kumar","Om Shankar","Bhanu Kumar","Manish Kumar"]
    mughal_slayers = ["Niraj Kumar","Vikaram Kumar","Nikhil Deol (Caption) ","Shaket Suman","Deobrat Raj"]
    gupta_crushers = ["Saroj Kumar","Vibhash Ranjan","Nishant Kumar","Rahul Singh (Caption) ","Hira Kumar"]
    #---------------------------------------
    pos = ["first","second"]  # Used to develop sentence like first team, second team.
    
    print("\nCheck what to press to select which team.....")  # Showing team list
    print("\n    ------------------International Teams----------------------")
    print("Press (I) ---- India                Press (WI) -- West Indies ")
    print("Press (A) ---- Australia            Press (SR) -- Sri Lanka  ")
    print("Press (E) ---- England              Press (NW) -- New Zealand ")
    print("Press (B) ---- Bangladesh           Press (SA) -- South_Africa ")
    time.sleep(1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("------------Teams of Patna-------   ---------Teams of India------------")
    print("Press (SW) -- Sipara Swingers        Press (CC) -- Chalukya Chargers")
    print("Press (BH) -- Beur Hitters           Press (GP) -- Gajapathi Panthers")
    print("Press (KA) -- Khajanchi Avengers     Press (MS) -- Mughal Slayers")
    print("Press (SS) -- Saguna Smashers        Press (GC) -- Gupta Crushers")
    time.sleep(2)


    for selection in range(2):
        while True: 
            team_chosen = input("\nselect the {} team: ".format(pos[selection]))
                
            if team_chosen.lower() == "i" :
                team_chosen = india
                team_ka_naam = "INDIA"
                break
            elif team_chosen.lower() == "a":
                team_chosen = australia
                team_ka_naam = "AUSTRALIA"
                break
            
            elif team_chosen.lower() == "e":
                team_chosen = england
                team_ka_naam = "ENGLAND"
                break
            
            elif team_chosen.lower() == "sa":
                team_chosen = south_africa
                team_ka_naam = "SOUTH AFRICA"
                break

            elif team_chosen.lower() == "b":
                team_chosen = bangladesh
                team_ka_naam = "BANGLADESH"
                break
            
            elif team_chosen.lower() == "wi":
                team_chosen = west_indies
                team_ka_naam = "WEST INDIES"
                break
            
            elif team_chosen.lower() == "sr":
                team_chosen = sri_lanka
                team_ka_naam = "SRI LANKA"
                break
            
            elif team_chosen.lower() == "nw":
                team_chosen = new_zealand
                team_ka_naam = "NEW ZEALAND"
                break

            elif team_chosen.lower() == "sw":
                team_chosen = sipara_swingers
                team_ka_naam = "SIPARA SWINGERS"
                break
            
            elif team_chosen.lower() == "bh":
                team_chosen = beur_hitters
                team_ka_naam = "BEUR HITTERS"
                break
            
            elif team_chosen.lower() == "ka":
                team_chosen = khajanchi_avengers
                team_ka_naam = "KHAJANCHI AVENGERS"
                break

            elif team_chosen.lower() == "ss":
                team_chosen = saguna_smashers
                team_ka_naam = "SAGUNA SMASHERS"
                break
            
            elif team_chosen.lower() == "cc":
                team_chosen = chalukya_chargers
                team_ka_naam = "CHALUKYA CHARGERS"
                break
            
            elif team_chosen.lower() == "gp":
                team_chosen = gajapathi_panthers
                team_ka_naam = "GAJAPATHI PANTHERS"
                break
            
            elif team_chosen.lower() == "ms":
                team_chosen = mughal_slayers
                team_ka_naam = "MUGHAL SLAYERS"
                break
            
            elif team_chosen.lower() == "gc":
                team_chosen = gupta_crushers
                team_ka_naam = "GUPTA CRUSHERS"
                break
            
            else: 
                print("invalid input ! Make input properly---")

        if selection==0:
            pahla_team = team_chosen
            first_team_name = team_ka_naam
            # print(pahla_team)
        else:
            dusra_team = team_chosen
            second_team_name = team_ka_naam
            # print(dusra_team)
        
while True:        #Taking mode to play ,also avoid getting wrong input.
    try:
        print("\n") 
        mode = int(input("Select the PLAY MODE .\n To play match individually, press 1.\n To play Quick match b/w teams,press 2.\nMake Your Choice and Hit Enter: ")) 
        print("--------------------------------------")
    except:
        print("\nyou can press only either 1 or 2 !Input again.")
    else:
        break

while True:
    if mode==1:
        no_of_teams=1
        count_team_member = 1
        playing_with_team = "no"
        print() 
        player_name = input("enter player name: ")
        print("     Welcome",player_name)

        break
    elif mode==2:
        no_of_teams=2
        playing_with_team = "yes"
        team_selection()        # function call
        count_team_member = 5
      
        break
    else:
        print("\nYou typed wrong input! Select mode correctly...")
        while True: 
            try:
                print("\n") 
                mode = int(input("Select the PLAY MODE .\n To play match individually, press 1.\n To play Quick match b/w teams,press 2.\nMake Your Choice and Hit Enter: ")) 
            except:
                print("you can press only either 1 or 2 !Input again.")
            else:
                break

while True:
    try:
        over = int(input("For how many overs you want to play: "))
        break        
    except:
        print("\nInvalid input ! Enter a proper number as a over") 
        print("________________________________________________")   

#----Different variables used in this program given below------
secondteam_win = 0   # to avoid problem of wickets of 2nd inning.(if second team wins ,then in the score last player is counted in fall of wickets so solve that ,this variable...used)
l1 = []  #first inning team total score
l2 = []  #second inning team total score
wickets = 0   #Represent the fall of wickets
point = "."     # Point is used to show over like 12.3 __12 overs 3 balls
total_score=0    # It counts the total score of a team
individual_score = 0  # It counts the individual player score 
run_per_ball = 0    # It counts run at each ball and added to individual player's score
list_first_team_score = []  #It consist of all team member of first team along with their score
list_second_team_score = []   #It consist of all team member of second team along with their score
total_balls = over*6  # it runs while loop
starting_ball = 1     #It count the ball along with score.,Helps to show the score of a player.
over_counting = 0      # Count over after every six ball played
numbering = 1    #representing balls of an over like 1st,2nd..
match_review=1   # gives review if run out,stumps
commentry = ""     #shows the commentry line at each shot or fall of wickets
freehit = 0       # take record of free hit
# ------------------------------------------------------
six=0      #Elaborating score display
four=0
one=0
two=0
three=0
wide=0
noball=0
d1={}
# --function to display full score of a player..
def detail_score_player():
    global d1,six,four,one,two,three,wide,noball 
    d1["SIX "]= six
    d1["FOUR "]= four
    d1["TRIPPLE "]= three
    d1["DOUBLE "]= two
    d1["SINGLE "]= one

    for s,r in d1.items():
        print("{} : {} ".format(s,r),end =" ,  ")
         # ------------------------------------------------
def to_empty_detail_score():
    global d1,six,four,one,two,three,wide,noball
    six=0     
    four=0
    one=0
    two=0
    three=0
    wide=0
    noball=0
    d1.clear()    
# ------------------------------------------------------------

            #  Developing TOSS System..--------------------
def toss_system():
    # temp = ""
    global temp,first_team_name,second_team_name,pahla_team,dusra_team,team_exchange,playing_with_team 
    toss_result = random.choice(["head","tail"])
    print("\n Team {} is requested to call for the toss \n Either PRESS 'h' for Head or 't' for  Tail ".format(second_team_name))
    while(True):
        toss = input("Make Your Call : ")
        if toss.lower()== "h" :
            toss_call = "head"
            break
        elif toss.lower() == "t":
            toss_call = "tail"
            break
        else: 
            print("\n __S0RRY__ ! You made wrong call......TRY AGAIN...\n")

    time.sleep(1)
    print(".....    ... ....    ....    ......  .....   .....   ......")
    time.sleep(1)
    print("             __________     ______     ______      ______  ")
    time.sleep(1)
    print("                 |         |      |   |      \    |      \  ")
    print("                 |         |      |   |______     |______   ")
    time.sleep(1)
    print("                 |         |      |          |           |  ")
    time.sleep(1)
    print("                 |         \______/   \______/    \______/  ")
    time.sleep(1)


    if toss_call == toss_result:
        print("\n      ..Team {} __WON__ the toss.. \n".format(second_team_name))
        while True: 
            first_do  = input("Team {} is requested to choose-----\nPRESS '1' to chose for Batting first \n    '2' to opt Bowling first -- : ".format(second_team_name))
            if first_do == '1':
                print("\n{} Opted to BAT First.$$".format(second_team_name))
                temp = first_team_name
                first_team_name = second_team_name
                second_team_name = temp

                team_exchange = pahla_team 
                pahla_team = dusra_team 
                dusra_team = team_exchange
                break 
            elif first_do == '2':
                print("\n{} Chosen  BOWLING First.@@".format(second_team_name))
                break
            else:
                print("\nyou are typing wrong input . Try anyway agian ---** \n")
        
    else: 
       
        print("\n      ..Team {} __WON__ the toss.. \n".format(first_team_name))
        while True: 
            first_do  = input("TEAM {} is requested to choose-----\nPRESS '1' to chose for Batting first \n    '2' to opt Bowling first -- : ".format(first_team_name))
            
            if first_do== '1':
                print("\n{} Opted to BAT First.$$".format(first_team_name))
                break 
            elif first_do== '2':
                print("\n{} Chosen  BOWLING First.@@".format(first_team_name))
                temp = first_team_name
                first_team_name = second_team_name
                second_team_name = temp

                team_exchange = pahla_team 
                pahla_team = dusra_team 
                dusra_team = team_exchange
                break
            else:
                print("\nyou are typing wrong input . Try anyway agian ---** \n")

# ---------------------------------------------------------------------
def welcome_message():
    global stadium,first_team_name,second_team_name
    stadium = random.choice(["Eden Garden stadium, KOLKATA","Chidambaram stadium , CHENNAI","Wankhede Stadium, MUMBAI","Green Park Stadium, KANPUR","Chinnaswamy Stadium, BENGLURU","Brabourne Stadium, MUMBAI","Barabati Stadium , CUTTACK","Holkar Stadium, INDORE","Melbourne Cricket Ground, AUSTRALIA","Rajiv Gandhi International Cricket Stadium, HYDERABAD"])
    print("\n           welcome to MATCH between {} and {} . ".format(first_team_name,second_team_name))
    print("               held at ___{}___ \n".format(stadium))
# --------------------------------------------------------------------
def showing_team_members():
    global pahla_team,dusra_team,first_team_name,second_team_name
    print("-----{}---------------------------{}------------     ".format(first_team_name,second_team_name))
    for i,j in zip(pahla_team,dusra_team):
        print("          {}                        {}          ".format(i,j))    

# ------------------------------TOSS FUNCTION CALL--------------------
if playing_with_team == "yes":
    toss_system()
    time.sleep(1)
    welcome_message()
    time.sleep(3)
    showing_team_members()
    time.sleep(6)
# -------------------------------------------------------------------
print("_____")
time.sleep(1)
print("     1 ONE")
time.sleep(1)
print("         TWO 2 ")
time.sleep(1)
print("            THREE 3")
time.sleep(1)
print("                 ARE YOU READY..........")
print("                   \ O /    ")
print("                     |      ")
print("                    / \     ")

print("\n       There goes the first over...")

# -----========___________
while(no_of_teams>0):

    while(count_team_member>0):
        
        if(playing_with_team=="yes" and total_balls>0):
            if(no_of_teams==2): 
                time.sleep(1)   
                print("\nPlayer on batting Now: {}".format(pahla_team[player_on_batting]))
            else:
                time.sleep(1 )
                print("\nPlayer on batting Now: {}".format(dusra_team[player_on_batting]))    
        
        while(total_balls>0):

            if (numbering%10==1 and numbering!=11):
                numb=str(numbering)+"st"
            elif (numbering%10==2 and numbering!=12):
                numb=str(numbering)+"nd"
            elif (numbering%10==3 and numbering!=13):
                numb=str(numbering)+"rd"
            else:
                numb=str(numbering)+"th"
            
            print("-----------------------------")
            
            let = input("enter letter 'a' and hit Enter to play the {} ball: ".format(numb))
            if let.lower()== "a":
                num = random.randint(1,14)
                
                if(num==1 or num==11):
                    commentry = random.choice(["wide ball","No Ball","Its just singal ","Off drive shot ,good one","Karibi mamla ho sakta tha Yaha pe\n reached in time","Oohohoho..Unnecessary run here ,Kharab bowling","Oh Get one on by---","What a reverse sweep","Tagara reverse sweep..","an upper cut shot .Luckly saved and gets a single.","Straight Drive bought a single.","No Ball","SQuare cut shot there ,...","Nicely taken single..","could have taken two but only single","good reverse shoot but only single","Run on by behind the keeper","cut at off side eaisly making a single","Ball pats down the left side .","There was no run there but someHow taken.","Nice stroke to get a single.","Its single....","You get only single.","You pats the ball on the off side and get a single","you plays it on the leg side & \n    jogs for a single","you taps the ball through the point and takes a single.","It was just a cut at leg side \n  and you get a nice single.","You get a single due to misfield","oo Its was a catch but missed and you get a single","Ya Here you could have taken 2 BUT \n you took only single","Nice single at off side","Straight down the ground but there is a fielder there\n    and you get only single"])
                    if commentry=="wide ball":
                        total_balls += 1 
                        numbering -= 1
                        print("___________")
                        print("|^ ##    ^|")
                        print("|  Wide   |")
                        print("|^   ##  ^|")
                        print("___________")

                        print(random.choice(["Here goes a wide ..adding 1 run to the score.","A Big Wide here at leg side..","a wide delivery given just now.","No confusion here Its wide Ball","It was a broad wide.","this one is wide,,.","a wide delivery.","Bowler may not happy with his wide ball."]))
                        wide +=1
                        total_score +=1
                        run_per_ball +=0

                    elif commentry=="No Ball":
                        total_balls += 1 
                        numbering -= 1
                        print("___________              __            ")
                        print("|^       ^|    |\  |   /    \          ")
                        print("|    1    |    | \ |  |      |   BALL  ")
                        print("|^       ^|    |  \|   \ __ /          ")
                        print("___________                            ")
                        print(random.choice(["Its just singal ","Off drive shot ,good one","Karibi mamla ho sakta tha Yaha pe\n reached in time","Oohohoho..Unnecessary run here ,Kharab bowling","Oh Get one on by---","What a reverse sweep","Tagara reverse sweep..","an upper cut shot .Luckly saved and gets a single.","Straight Drive bought a single.","SQuare cut shot there ,...","Nicely taken single..","could have taken two but only single","good reverse shoot but only single","Run on by behind the keeper","cut at off side eaisly making a single","Ball pats down the left side .","There was no run there but someHow taken.","Nice stroke to get a single.","Its single....","You get only single.","You pats the ball on the off side and get a single","you plays it on the leg side & \n    jogs for a single","you taps the ball through the point and takes a single.","It was just a cut at leg side \n  and you get a nice single.","You get a single due to misfield","oo Its was a catch but missed and you get a single","Ya Here you could have taken 2 BUT \n you took only single","Nice single at off side","Straight down the ground but there is a fielder there\n    and you get only single"]))
                        print()
                        print(random.choice(["Its No Ball.$ You get a free hit .","O No .! Its  No Ball and Free hit,,","Its No Ball ,Its Free hit","The Umpire's Decision N0 Ball","No BALL ,The Batsman gets a Free HiT.","Umpire found N0 Ball here......"]))
                        noball+=1
                        one+=1
                        total_score +=2
                        run_per_ball +=1

                    else:
                        print("___________")
                        print("|^       ^|")
                        print("|    1    |")
                        print("|^       ^|")
                        print("___________")
                        print(commentry)
                        one+=1
                        total_score +=1
                        run_per_ball +=1
                
                elif(num==2 or num==12):
                    print("___________")
                    print("| ^     # |")
                    print("|    2    |")
                    print("| %     $ |")
                    print("___________")
                    commentry = random.choice(["What a running between the wickets..taken 2","The second one was risky but taken.","Muskil tha dusra run but batsman did it","No Ball","an easy off Drive shot, ran for two","Taken two due to misfield","two runs taken nicely","Paddle sweep straight forward.","Bahari kinara good luck and taken 2","Completed two runs eaisly","Unnecessary throw ,made batsman to go for two.","this throw was not needed here ,given two instead of one","Hard hit shot but fielders restricted to only 2","Its double......","Very good running between the wickets. ","Superb running ,done two."])
                    if commentry=="No Ball":
                        total_balls += 1 
                        numbering -= 1
                        noball +=1
                        two +=1
                        total_score += 3
                        run_per_ball+=2
                        print(random.choice(["What a running between the wickets..taken 2","The second one was risky but taken.","Muskil tha dusra run but batsman did it","an easy off Drive shot, ran for two","Taken two due to misfield","two runs taken nicely","Paddle sweep straight forward.","Bahari kinara good luck and taken 2","Completed two runs eaisly","Unnecessary throw ,made batsman to go for two.","this throw was not needed here ,given two instead of one","Hard hit shot but fielders restricted to only 2","Its double......","Very good running between the wickets. ","Superb running ,done two."]))
                        print()
                        print(random.choice(["Its No Ball.$ You get a free hit .","O No .! Its  No Ball and Free hit,,","Its No Ball ,Its Free hit","The Umpire's Decision N0 Ball","No BALL ,The Batsman gets a Free HiT.","Umpire found N0 Ball here......"]))
                    else:
                        print(commentry)
                        two +=1
                        total_score +=2
                        run_per_ball+=2

                elif(num==3):
                    print("___________")
                    print("| !!   !! |")
                    print("|    3    |")
                    print("|  _   _  |")
                    print("___________")
                    commentry = random.choice(["The batsman rocks onto the back foot and punches the ball.","Very good running between the wickets","The batsman played towards leg side and eaisly taken 3","Behtarin filding yaha par,saves one run for the team","No Ball","Good Running ,an easy Tripple","Two taken and a leg bye to the end .","Thats a lovely shot ,good run","Wao,Batsman made it tripple..","risk taken here but successfully done 3 ","It was a risky tripple here","Oho..There was no need to throw here , Batting team gets an extra","good stroke and made it to three","Nice fielding to stop a boundry","On middle , pushed down to long on for a run,,","Full on middle and driven towards mid on.","Ball passed between the filders.","It was only one here but got three on by.","Unnecessary  ONE  extra  run here ","Leg side,steered behind point for 3 ","Full and outside Off,driven through for the three","A Short ball ,around middle securing three run","Outside Off,Pushed straight to cover and get three","It goes near the boundry.\n  But You get 3 runs.."])
                    if commentry=="No Ball":
                        total_balls += 1 
                        numbering -= 1
                        noball+=1
                        three +=1
                        total_score += 4
                        run_per_ball += 3
                        print(random.choice(["It goes near the boundry.\n  But You get 3 runs.."]))
                        print()
                        print(random.choice(["Its No Ball.$ You get a free hit .","O No .! Its  No Ball and Free hit,,","Its No Ball ,Its Free hit","The Umpire's Decision N0 Ball","No BALL ,The Batsman gets a Free HiT.","Umpire found N0 Ball here......"]))
                    else:
                        print(commentry)
                        three +=1
                        total_score +=3
                        run_per_ball += 3

                elif(num==4):
                    print("___________")
                    print("|  *   *  |         o   o   ")
                    print("|    4    |           |     ")
                    print("|  *   *  |         \___/   ")
                    print("___________")
                    commentry = (random.choice(["FOUR! That's excellent timing!","Two BOUNCE chauka right now here.","Fantastic shot leading to ONE BOUNCE boundry ....","Batsman goes back and cuts it behind point leading it to the boundry line.","No Ball","FOUR -- LEG BYYE.Down the leg side.","Nice boundry with the reverse sweep,Bowler is disappointed here.","Its one Bounce chauka.^^","oh. Filder losses caught and giver a boundry.Double benifits to the Batsman","That's a proper cricket shot leading to a Boundry.","0ooo... Its a Boundry for a Four..","``~~FOUR! A full Toss ,outside off","That's Low full toss and batsman takes to the Boundry","FOUR!TONK! Alength ball, following the batsman,down the leg side","oNe Bounce boundry goes for a FOUR.","Full and in line of the stumps,\n batsman backs away and hammers it straight back over the bowler.","THUNDEROUS! Short and outside off,\nBatsman backs away and slaps it over point for a boundry!","Cracking shot this was..Nice boundry","THUMP! A short ball, around middle,\nBatsman pulls this behind square leg and finds the boundry","Boundry ,This time with good timming.^","Nice chauka at leg side","Straight down the ground and there goes a boundry.","Chauka due to misfield of keeper.","Kharab filding yaha par,\n Ball cheat the filder's hand and crossed the boundry line."]))
                    if commentry=="No Ball":
                        total_balls += 1 
                        numbering -= 1
                        noball+=1
                        four+=1
                        total_score += 5
                        run_per_ball += 4
                        print(random.choice(["0ooo... Its a Boundry for a Four..","Nice chauka at left side","Straight down the ground and there goes a boundry.","Chauka due to misfield of keeper.","Kharab filding yaha par,\n Ball cheat the filder's hand and crossed the border."]))
                        print()
                        print(random.choice(["Its No Ball.$ You get a free hit .","O No .! Its  No Ball and Free hit,,","Its No Ball ,Its Free hit","The Umpire's Decision N0 Ball","No BALL ,The Batsman gets a Free HiT.","Umpire found N0 Ball here......"]))
                    else:
                        print(commentry)
                        four+=1
                        total_score +=4
                        run_per_ball += 4

                elif(num==5):
                    print("___________")
                    print("|         |         o   o   ")
                    print("|   0UT   |         : | :   ")
                    print("|         |          ___   ")
                    print("___________         '   '  ")
                    
                    commentry = "out Hai"
                    out =random.choice(["run out","caught out","clean bold","stump","LBW"])
                    if freehit == 1 and out!= "run out":
                        print("you are {} on this delivery BUT safe due to Free Hit".format(out))
                        freehit=0
                    else:
                        if freehit == 1:
                            print("Free hit won't work in case of Run 0ut.")
                            freehit = 0    
                        print("Original Decision: {}".format(out))
                        if out=="run out" or out== "stump" or out=="LBW":
                            karibi_mamla = random.choice(["2","3","4"])
                            if out=="run out":
                                print(random.choice(["Its a direct hit ..","ohoho you are run out.","What a tremendous direct hit and gone.","There goes a run out.","Siit ! yaar run out!!"]))
                                run_out_runs = random.choice([0,2,0,0,0,0,1])
                                print()
                                print("You are Run Out While taking ",run_out_runs+1)
                                total_score += run_out_runs
                                run_per_ball += run_out_runs
                                if run_out_runs==2:
                                    two+=1
                                elif run_out_runs==1:
                                    one+=1
                                else:
                                    pass
                            elif out=="LBW":
                                print(random.choice(["LBW Out","Its leg before wicket","Ball hits the pad and he is gone.","the Umpire raised his hand up for the LBW","Gone here by the LBW","The batsman played the ball with the pad and gone","The ball went straight and hits the pad\nthe result is LBW","right decision ,Its LBW"]))
                            else:
                                print(random.choice(["oo what a stump!","wounderful stump."," you are stump out"]))
                            
                            if karibi_mamla=="2" or karibi_mamla=="4":
                                
                                print(random.choice(["      karibi mamla yaha per,The batting team may go for the review.","        The difficult movement here,the player may go out","       karibi mamla ho sakta hai yaha..","              It happend with a fraction of second , bowling team may go for the review.","               If required ,Review can be taken.","                Bahut hi najdiki mamla ho sakta hai ** ",               "Difficult`` Umpire took some time to give the Decision."]))
                                if(match_review>0):
                                    while True:
                                        try:
                                            take_review = int(input("\n Press 1 to take review and Hit Enter \n Otherwise to continue press any number and Hit Enter: "))
                                            break 
                                        except:
                                            print("\nWrong input! Make valid input to review.")
                                            print("___________")
                                    if (take_review==1):
                                        decision = random.choice(["Out","Not Out","Out"])
                                        if decision == "Out":
                                            print()
                                            time.sleep(1)
                                            print("             ---------------------- ")
                                            time.sleep(1)
                                            print("             |  DECISION PENDING  | ")
                                            time.sleep(1)
                                            print("             ---------------------- ")
                                            time.sleep(1)
                                            print("Third Empire Decision: Out")
                                            print("\nYou loose your review!")
                                            match_review -=1
                                            print("\n")

                                            if(playing_with_team=="yes"):
                                                individual_score += run_per_ball
                                                
                                                run_per_ball = 0
                                                break
                                                                    
                                            else:
                                                print("your total_score is {} Runs out of {} Balls ".format(total_score,starting_ball - (wide+noball)))
                                                break
                                        else:
                                            print()
                                            time.sleep(1)
                                            print("             ---------------------- ")
                                            time.sleep(1)
                                            print("             |  DECISION PENDING  | ")
                                            time.sleep(1)
                                            print("             ---------------------- ")
                                            time.sleep(1)
                                            print("Third Empire Decision: Not Out")
                                            print("\nYou save your review!") 
                                            
                                    else :
                                        print("\n")
                                        if(playing_with_team=="yes"):
                                            individual_score += run_per_ball
                                            
                                            run_per_ball = 0
                                            break
                                        else:
                                            print("your total_score is {} Runs out of {} Balls ".format(total_score,starting_ball - (wide+noball)))
                                            break
                                else:
                                    print("\n           ------------  No Review Available ! ----------")
                                    if(playing_with_team=="yes"):
                                        individual_score += run_per_ball
                                
                                        run_per_ball = 0
                                        break
                                    else:
                                        print("your total_score is {} Runs out of {} Balls ".format(total_score,starting_ball - (wide+noball)))
                                        break
                                            
                            else:
                                    
                                print("\n")
                                if(playing_with_team=="yes"):
                                    individual_score += run_per_ball
                                    
                                    run_per_ball = 0
                                    break
                                else:
                                    print("your total_score is {} Runs out of {} Balls ".format(total_score,starting_ball - (wide+noball)))
                                    break
                            
                                
                        else:
                            if(out=="clean bold"):
                                print(random.choice(["OO you are clean bold ","aahh!! Its clean Bold.","Ball Hits the mid wicket."]))
                            else:                
                                print(random.choice(["WAO. Its wounder catch and you got out...","The ball was very much high but covered no distance \n and got caught up by keeper itself.","Bowler himself caught the catch and you are out.","What a catch at the boundry area.Fantastic.\n But you have to move to the pavilion."]))
                            print("\n")
                            if(playing_with_team=="yes"):
                                individual_score += run_per_ball
                                
                                run_per_ball = 0
                                break
                            else:
                                print("your total_score is {} Runs out of {} Balls ".format(total_score,starting_ball - (wide+noball)))
                                break

                        
                elif(num==8 or num==10):
                    print("___________")
                    print("|         |")
                    print("|  Missed |")
                    print("|         |")
                    print("___________")
                    commentry = (random.choice(["Batsman misses the ball.","ooo, slightly missed otherwise it would be stump here.","Nice appeal here but Umpire has no intention to give out.","ONE BOUNCER here ,,","Ball passes leaving bat untouched .","A Testing bouncer ,around middle,Batsman is late on the hook.","A short ball,batsman has a good chance here but left.","Batsman leaves the ball","Batsman was completely baffled by this delivery","Tried hitting for boundry but missed!!!","No Ball"]))
                    if commentry=="No Ball":
                        total_balls += 1 
                        numbering -= 1
                        noball+=1
                        total_score += 1
                        run_per_ball += 0
                        print(random.choice(["Batsman misses the ball.","A short ball outside off,Batsman looks to pull but misses","ooo, slightly missed otherwise it would be stump here.","Nice appeal here but Umpire has no intention to give out.","ONE BOUNCER here ,,","Ball passes leaving bat untouched .","A Testing bouncer ,around middle,Batsman is late on the hook.","A short ball,batsman has a good chance here but left.","Batsman leaves the ball","Batsman was completely baffled by this delivery","Tried hitting for boundry but missed!!!"]))
                        print()
                        print(random.choice(["Its No Ball.$ You get a free hit .","O No .! Its  No Ball and Free hit,,","Its No Ball ,Its Free hit","The Umpire's Decision N0 Ball","No BALL ,The Batsman gets a Free HiT.","Umpire found N0 Ball here......"]))
                    else:
                        print(commentry)
                        total_score +=0
                        run_per_ball += 0
                
                elif(num==9 or num==13):
                    print("___________")
                    print("|    *    |")
                    print("| Nothing |")
                    print("|    *    |")
                    print("___________")
                    commentry = (random.choice(["A touch short,the googly,around off.","Missed ..No run.","Nice filding there ,batsman were restricted to take even single","Ball was tapped but no run","Around off, defended solidly.","On middle,driven througn mid on but no run","A short ball,down the leg side , missed by the batsman","Around off, defended from the crease.","full and around off, pushed back to the bowler","good fielding!shorter and leg side driven."]))
                    print(commentry)
                    total_score +=0
                    run_per_ball += 0

                elif(num==7 or num==14):
                    print("___________")
                    print("|   Nice  |")
                    print("|    *    |")
                    print("|   Ball  |")
                    print("___________")
                    commentry = (random.choice(["Excellent Yorker,tergetting the stumps\n  But Player somehow put down the bat in time","a terrific yorker,dug out back to the bowler.","Yorker,around middle,dug out towards cover but no run","Excellent Yorker,Batsman baffled completely","Bowling a Good Line and Length","Fantastic ball & No run.....","The Googly now, outside off,short in length.","a length ball around off","A slower and shorter in length.","Shorter and on middle,batsman failed to get a single","HaHa.. little more turn could have taken the batsman to the pavilion.","What! a ball it is..","The ball just moved out from keeper's hand \nAND you are safe now..","It was just a cut..","Nice bowling..","What a bouncer ! ek dam dhakar..","superb googly ball","The ball left untouched to the bat."]))
                    print(commentry)
                    
                else:
                    print("___________")
                    print("|  *  *   |        \  O  /   ")
                    print("| *  6  * |         --|--     ")
                    print("|  *  *   |          / \      ")
                    print("___________")
                    commentry = (random.choice(["waooo..Its a massive SiX..","Knee drop down the ground and made it a six.","An Eaisy six this one,Just raised the bat\n  and ball goes automatically to the boundry line.","Tagara shot ,Ball jumps out to the boundry for a wounderfull six. ~~","SIX ! What the shot it was mesmerizing","An impressive SIX .","Ball in the air, crossed the boundry line and goes for a six.","What an astonished shot ! S I X ","No Ball","Its a Straight s i x. ","The ball goes high and high and dropped down just On the boundry line.","No Fielder there , A Low height 6","SIX ! THRASH ! Full and outside Off","Batsman massively sweeps this over mid-wicket and goes for a six.","A Low full Toss given here, and batsman took it to the boundry ","oo .. << six on bouncer ","Made six ,straight forward and the bowler is disappointed here.","Kharab bowling, and gives  a massive six to the opponent.","The ball was good but the batsman left no mercy and took it for a S I X","Merciless Hitting to the ball and 6","Its a six,Making this one on a Full Toss.","Full Toss and It goes no way but directly to the boundry line","Waoo.. Fielders could only see the ball going over head for a SIX.","The ball flies away for a six.","You jumps out and hits over a point for a huge SIX."]))
                    if commentry=="No Ball":
                        total_balls += 1 
                        numbering -= 1
                        noball+=1
                        six+=1
                        total_score += 7
                        run_per_ball += 6
                        print(random.choice(["waooo..Its a massive SiX..","You jumps out and hits over a point for a huge SIX."]))
                        print()
                        print(random.choice(["Its No Ball.$ You get a free hit .","O No .! Its  No Ball and Free hit,,","Its No Ball ,Its Free hit","The Umpire's Decision N0 Ball","No BALL ,The Batsman gets a Free HiT.","Umpire found N0 Ball here......"]))
                    else:
                        print(commentry)
                        six+=1
                        total_score +=6
                        run_per_ball += 6
            
            else:
                print("\nYou misses the ball,Since you put *Invalid input* !i!")

            # -----------after ball played---- 
            print("\n\n")   
            if(playing_with_team=="yes"):
                individual_score += run_per_ball
                run_per_ball = 0
            
            total_balls-=1
            if (no_of_teams==1 and playing_with_team=="yes" and total_balls!=0): #condition for 2nd inning only
                if total_score > score_first_team:
                    secondteam_win = 1
                    break

            if commentry!="wide ball":
                freehit = 0       #after completion of free hit ball ,freehit becomes zero.

            if commentry == "No Ball":
                freehit = 1
            
            if(numbering==6):
                numbering=0
                over_counting += 1
                if(playing_with_team=="yes"):
                    if (no_of_teams==2):
                        print("=========================================")   
                        print("{} : {} runs / {} balls".format(pahla_team[player_on_batting],individual_score,starting_ball - (wide+noball)))
                        print("\n{} : {} /{} wickets  ,over: {}{}{}".format(first_team_name,total_score,wickets,over_counting,point,numbering))
                        
                    else:
                        print("=========================================")
                        print("{} : {} runs / {} balls".format(dusra_team[player_on_batting],individual_score,starting_ball - (wide+noball)))
                        print("\n{} : {} /{} wickets  ,over: {}{}{}".format(second_team_name,total_score,wickets,over_counting,point,numbering))
                        
                        
                else:
                    print("\nyour total_score is {} Runs of {} Balls ".format(total_score,starting_ball - (wide+noball)))
                    print("       {} over is completed! ".format(over_counting))     
                
                print("-----------------------------------------")
                
            if(playing_with_team=="yes" and total_balls==0):
                if (no_of_teams==2):   #condition for first inning
                    # detail_score_player()
                    list_first_team_score.append(" {} :  {} Runs/{} Balls   ,{} SIX / {} FOUR".format(pahla_team[player_on_batting],individual_score,starting_ball - (wide+noball),six,four))
                    to_empty_detail_score()
                else:  # condition for second inning
                    # detail_score_player()
                    list_second_team_score.append(" {} :  {} Runs/{} Balls   ,{} SIX / {} FOUR".format(dusra_team[player_on_batting],individual_score,starting_ball - (wide+noball),six,four))
                    to_empty_detail_score()
            
                

            numbering +=1
            starting_ball +=1
            
            # ----------------total_balls>0 breaks here-----2nd loop---starts--
        
        if(playing_with_team=="yes" and total_balls>0):
            total_balls-=1
            
            if(numbering==6): #if a player gets out at 6th ball..
                numbering=0
                over_counting += 1
                
                print("-----------------------------------")
                
            
            if (no_of_teams==2):   #condition for first inning ****  In this loop ,complier comes when a player is out.
                wickets +=1
                print("=========================================")
                print("{} : {} runs / {} balls".format(pahla_team[player_on_batting],individual_score,starting_ball - (wide+noball)))
                detail_score_player()
                print()
                
                print("\n{} : {} runs/{} wickets  ,over: {}{}{}".format(first_team_name,total_score,wickets,over_counting,point,numbering))
                list_first_team_score.append(" {} :  {} Runs/{} Balls   ,{} SIX / {} FOUR".format(pahla_team[player_on_batting],individual_score,starting_ball - (wide+noball),six,four))
                to_empty_detail_score()
                # print(list_first_team_score)
            else:  # condition for second inning
                if secondteam_win != 1:
                    wickets += 1
                print("=========================================")
                print("{} : {} runs / {} balls".format(dusra_team[player_on_batting],individual_score,starting_ball - (wide+noball)))
                detail_score_player()
                print()
                
                print("\n{} : {} /{} wickets  ,over: {}{}{}".format(second_team_name,total_score,wickets,over_counting,point,numbering))
                list_second_team_score.append(" {} :  {} Runs/{} Balls   ,{} SIX / {} FOUR".format(dusra_team[player_on_batting],individual_score,starting_ball - (wide+noball),six,four))
                to_empty_detail_score()

            numbering +=1
            if (no_of_teams==1 and playing_with_team=="yes"): #condition for 2nd inning only
                if total_score > score_first_team:
                    break


            starting_ball = 1   
            
        individual_score = 0
        count_team_member -=1
        player_on_batting+=1

    # -----------------------all player is out in 1st inning---

    # -----------Starting of 2nd inning----------
    if(no_of_teams==2):              # Applicable only for 2nd inning  starting.
        l1.append("{} : {} runs/{} wickets  ,over: {}{}{}".format(first_team_name,total_score,wickets,over_counting,point,numbering-1))
        wickets_fall_first_team = wickets
        total_balls = 0
        total_balls = over*6
        numbering = 1
        starting_ball = 1
        wickets = 0
        count_team_member=5
        player_on_batting=0
        over_counting = 0
        match_review = 1
        score_first_team = total_score
        total_score=0
        time.sleep(1)
        print("\n    @@@@ ---  FIRST INNING COMPLETED   ----  @@@@ \n")
        time.sleep(1)
        print("__________________________________")
        print("Now its Turn of second innings.....")
      
        print("\nTeam on Batting: {}".format(second_team_name))

    if (no_of_teams==1 and playing_with_team=="yes"):
        l2.append("{} : {} runs/{} wickets  ,over: {}{}{}".format(second_team_name,total_score,wickets,over_counting,point,numbering-1))
    no_of_teams -=1
# -------END of  1st LOOP -------------------------------

if(playing_with_team=="yes" ):
    score_second_team = total_score
    print("________________________________________________")
    print(l1[0])  #shows the score of first team 
    print(l2[0])  #shows the score of second team
    print("________________________________________________")
    if (score_first_team > score_second_team):
        print("\n     **@  CONGRATULATION  @** --- To team {} \n {} wins by {} runs...**".format(first_team_name,first_team_name,score_first_team - score_second_team))
    elif (score_first_team < score_second_team):
        print("\n     **@  CONGRATULATION  @** --- To team {} \n {} wins by {} wickets...**".format(second_team_name,second_team_name,len(pahla_team) - wickets))    
        
    else:
        print("GAME RESULT : ** ___DRAW___ ** ")

    while True:
        print()
        end_match_score = input("PRESS ---( M )---- to get the detail score of match and hit enter..\n otherwise anY letter to EXIT and hit enter:  ")
        if end_match_score.lower()== "m" :
            
            print("\n\n     ____  MATCH SCORE  ____ ")
            print("_____________________________________________________")
            print(l1[0])  #shows the score of first team
            print()
            for score_a in list_first_team_score:
                print(score_a)
            print("----------------------------------------------------")
            print(l2[0])  #shows the score of second team
            print()
            for score_b in list_second_team_score:
                print(score_b)
            print("_____________________________________________________")
            print()
            break
        
        else:
            
            break


# Display single player score ...
if (playing_with_team=="no" ):
    print("Player's Score in Detail :----\n")
    print("Player Name: ",player_name)
    detail_score_player()
    print("\n")

print()
print("       -\/'''````\___ T H A N K  *  Y O U  ___/````''''\/-")
print()


getch = input("\n\n .......  HIT ENTER to exit Console  .....")