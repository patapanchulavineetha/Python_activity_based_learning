

1. COMPUTATIONAL THINKING BREAKDOWN

*Decomposition:*
1.  Collect 10 maintenance reports
2.  Define severity, location, frequency weights
3.  Apply rules to calculate priority
4.  Rank cases
5.  Generate summary

*Pattern Recognition:*
- Critical severity always = P1
- Lab/Hostel = more critical location
- Daily frequency = more urgent

*Abstraction:*
Incident = [ID, Description, Severity, Location, Frequency, Type]

*Algorithm Design:* Rule-based scoring

2. ALGORITHM (Step-by-step)
START
  Initialize incidents as nested list of 10 cases
  Initialize critical_locations as tuple
  Initialize severity_levels tuple (Critical,4) etc
  Initialize frequency_scores tuple (Daily,3) etc
  Initialize prioritized_list empty

  DEFINE function get_severity_score(sev):
    FOR each (s,score) in severity_levels:
      IF s == sev: RETURN score
    RETURN 0

  DEFINE function get_freq_score(freq):
    FOR each (f,score) in frequency_scores:
      IF f == freq: RETURN score
    RETURN 0

  DEFINE function calculate_priority(sev, loc, freq):
    sev_score = get_severity_score(sev)
    freq_score = get_freq_score(freq)
    loc_weight = 2 if loc in critical_locations else 1
    total_score = sev_score*2 + freq_score + loc_weight
    
    IF sev == "Critical": priority = "P1-EMERGENCY"
    ELSE IF sev=="High" AND freq=="Daily" AND loc in critical_locations: priority="P1-EMERGENCY"
    ELSE IF sev=="High" AND (freq=="Daily" OR freq=="Weekly"): priority="P2-HIGH"
    ELSE IF sev=="Medium" AND freq=="Daily" AND loc=="Lab": priority="P2-HIGH"
    ELSE IF sev=="Medium" OR (sev=="High" AND freq=="Rare"): priority="P3-MEDIUM"
    ELSE: priority="P4-LOW"
    RETURN priority, total_score

  LOOP menu:
    1. View 10 cases
    2. Classify -> call calculate_priority for each -> store in prioritized_list
    3. Sort prioritized_list by score descending using bubble sort (nested loops)
    4. Generate summary report (count P1,P2,P3,P4)
  END LOOP
END
3. FLOWCHART (Text format for drawing)
[START] -> [Initialize 10 cases nested list, tuples]
-> [Display Menu] -> [Choice?] 
   -> 1: [Loop through incidents] -> [Display using unpacking] -> [Menu]
   -> 2: [For each incident -> calculate priority -> calculate score] -> [Bubble Sort Loop i,j] -> [Display Ranked List] -> [Menu]
   -> 3: [Input search string -> Loop + string lower() contains check] -> [Menu]
   -> 4: [Input new incident -> Validate severity/frequency using conditionals] -> [Append to nested list] -> [Menu]
   -> 5: [Count P1,P2,P3,P4 using loops] -> [Pattern # chart] -> [Location summary loop] -> [Menu]
   -> 6: [Pattern Generation **** -> END]
4. PSEUDOCODE
SET incidents = [
  ["INC01","Lab Power Failure","Critical","Lab","Daily","Electrical"],
  ...10 cases
]
SET critical_locations = ("Lab","Hostel","Washroom")
SET severity_levels = (("Critical",4),("High",3),("Medium",2),("Low",1))
SET frequency_scores = (("Daily",3),("Weekly",2),("Rare",1))

FUNCTION calculate_priority(sev, loc, freq):
  FIND sev_score FROM severity_levels
  FIND freq_score FROM frequency_scores
  IF loc IN critical_locations: loc_weight=2 ELSE loc_weight=1
  total = sev_score*2 + freq_score + loc_weight
  APPLY IF-ELIF rules to get priority string
  RETURN priority, total

WHILE True:
  PRINT Menu
  READ choice
  IF choice=="2":
    FOR each incident in incidents:
      UNPACK iid, desc, sev, loc, freq, typ = incident
      CALL calculate_priority(sev,loc,freq)
      APPEND [iid,desc,sev,loc,freq,typ,priority,score] to prioritized_list
    FOR i in 0 to len-1:
      FOR j in 0 to len-i-2:
        IF prioritized_list[j][7] < prioritized_list[j+1][7]:
          SWAP
    PRINT ranked list
    5.Python code
incidents = [
    ["INC01", "Lab System Power Failure - CSE Lab", "Critical", "Lab", "Daily", "Electrical"],
    ["INC02", "Water Leakage in Girls Hostel", "High", "Hostel", "Daily", "Plumbing"],
    ["INC03", "Projector Not Working - Classroom 301", "Medium", "Classroom", "Weekly", "Electrical"],
    ["INC04", "Library AC Not Cooling", "Low", "Library", "Rare", "HVAC"],
    ["INC05", "Washroom Drainage Block - Main Block", "High", "Washroom", "Daily", "Plumbing"],
    ["INC06", "WiFi Router Failure - ECE Dept", "Critical", "Lab", "Daily", "Network"],
    ["INC07", "Canteen Hygiene - Food Waste", "Medium", "Canteen", "Weekly", "Cleaning"],
    ["INC08", "Broken Bench in Classroom 101", "Low", "Classroom", "Rare", "Furniture"],
    ["INC09", "Fire Alarm Sensor Beeping - Hostel", "Critical", "Hostel", "Daily", "Safety"],
    ["INC10", "Parking Area Light Failure", "Medium", "Parking", "Weekly", "Electrical"]
]

critical_locations = ("Lab", "Hostel", "Washroom")
severity_levels = (("Critical", 4), ("High", 3), ("Medium", 2), ("Low", 1))
frequency_scores = (("Daily", 3), ("Weekly", 2), ("Rare", 1))

prioritized_list = []

def get_severity_score(sev):
    for s, score in severity_levels:  # tuple unpacking
        if s == sev:
            return score
    return 0

def get_freq_score(freq):
    for f, score in frequency_scores:
        if f == freq:
            return score
    return 0

def calculate_priority(severity, location, frequency):
    sev_score = get_severity_score(severity)
    freq_score = get_freq_score(frequency)
    loc_weight = 2 if location in critical_locations else 1
    total_score = sev_score * 2 + freq_score + loc_weight
    
    if severity == "Critical":
        priority = "P1-EMERGENCY"
    elif severity == "High" and frequency == "Daily" and location in critical_locations:
        priority = "P1-EMERGENCY"
    elif severity == "High" and (frequency == "Daily" or frequency == "Weekly"):
        priority = "P2-HIGH"
    elif severity == "Medium" and frequency == "Daily" and location == "Lab":
        priority = "P2-HIGH"
    elif severity == "Medium":
        priority = "P3-MEDIUM"
    elif severity == "High" and frequency == "Rare":
        priority = "P3-MEDIUM"
    else:
        priority = "P4-LOW"
    return priority, total_score

MAIN LOOP
while True:
    print("\n" + "="*60)
    print("SMART CAMPUS INCIDENT PRIORITIZATION")
    print("="*60)
    print("1. View 10 Cases\n2. Classify & Rank\n3. Search\n4. Add Incident\n5. Summary Report\n6. Exit")
    ch = input("Choice: ").strip()

    if ch == "1":
        for i in range(1,4):
            print("*"*i + " CASE STUDIES " + "*"*i)
        for inc in incidents:
            iid, desc, sev, loc, freq, typ = inc
            print(f"{iid} | {sev} | {loc} | {freq} | {desc} [{typ}]")

    elif ch == "2":
        prioritized_list = []
        for inc in incidents:
            iid, desc, sev, loc, freq, typ = inc
            prio, score = calculate_priority(sev, loc, freq)
            prioritized_list.append([iid, desc, sev, loc, freq, typ, prio, score])
        
        # Bubble Sort - syllabus loop method
        for i in range(len(prioritized_list)):
            for j in range(len(prioritized_list)-i-1):
                if prioritized_list[j][7] < prioritized_list[j+1][7]:
                    prioritized_list[j], prioritized_list[j+1] = prioritized_list[j+1], prioritized_list[j]
        
        print(f"\n{'ID':<7} {'PRIORITY':<13} {'SCORE':<5} Details")
        for p in prioritized_list:
            iid, desc, sev, loc, freq, typ, prio, score = p
            print(f"{iid:<7} {prio:<13} {score:<5} {desc} @ {loc}")

    elif ch == "5":
        if len(prioritized_list)==0:
            for inc in incidents:
                iid, desc, sev, loc, freq, typ = inc
                prio, score = calculate_priority(sev, loc, freq)
                prioritized_list.append([iid, desc, sev, loc, freq, typ, prio, score])
        
        p1=p2=p3=p4=0
        for p in prioritized_list:
            if "P1" in p[6]: p1+=1
            elif "P2" in p[6]: p2+=1
            elif "P3" in p[6]: p3+=1
            else: p4+=1

        print("\n" + "="*50)
        print(f"Total: {len(prioritized_list)} | P1:{p1} P2:{p2} P3:{p3} P4:{p4}")
        print("Chart:")
        for label, count in [("P1-EMERGENCY",p1), ("P2-HIGH",p2), ("P3-MEDIUM",p3), ("P4-LOW",p4)]:
            print(f"{label}: {'#'*count} ({count})")
        
        print("\nAction Plan:")
        for p in prioritized_list:
            iid, desc, sev, loc, freq, typ, prio, score = p
            if "P1" in prio: action="Fix in 2 Hours"
            elif "P2" in prio: action="Fix in 24 Hours"
            elif "P3" in prio: action="Fix in 3 Days"
            else: action="Fix in a Week"
            print(f"{prio} - {iid} {loc}: {action}")

    elif ch == "6":
        for i in range(5,0,-1):
            print("*"*i)
        print("Exiting")
        break
