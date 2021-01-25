from position import Position

#future ideas (show cost per month in a table, cost per position, location-based multipliers)
#add assumptions to printout
def main():

    print("This tool is meant to provide budgetary estimate of internal resources needed") 
    print("to get an oil/gas/chemicals project from concept to an investment decision:")
    print("===============================================")
    print("What is the approximate project size (in M$)?")
    print("1. 0 - 10 M$ ")
    print("2. 11 - 40 M$ ")
    print("3. 41 - 100 M$ ")
    print("4. 101 - 500 M$ ")
    print("5. >500 M$ ")
    print("> ",)
    user_input_size = input()

    print()
    print("What type of industry is your project?")
    print("1. Refining") #base case, multiply by 1.0
    print("2. Chemicals") #more complex, multiply by 1.1
    print("3. Upstream - on land") #multiply by 1.2
    print("4. Upstream - on water") ##multiply by 1.3
    print("> ",)
    user_input_industry = input()


#---------0-10M$ projects-------------
    if user_input_size == "1" and user_input_industry == "1":
    #Object oriented programming!
        total = 0
        project_size = "0-10M"
        industry = "Refining"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")
    
    elif user_input_size == "1" and user_input_industry == "2":
        total = 0
        project_size = "0-10M"
        industry = "Chemicals"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "1" and user_input_industry == "3":
        total = 0
        project_size = "0-10M"
        industry = "Upstream - on land"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "1" and user_input_industry == "4":
        total = 0
        project_size = "0-10M"
        industry = "Upstream - on water"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

#---------11-40M$ projects-------------
    elif user_input_size == "2" and user_input_industry == "1":
        total = 0
        project_size = "11-40M"
        industry = "Refining"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "2" and user_input_industry == "2":
        total = 0
        project_size = "11-40M"
        industry = "Chemicals"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "2" and user_input_industry == "3":
        total = 0
        project_size = "11-40M"
        industry = "Upstream - on land"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "2" and user_input_industry == "4":
        total = 0
        project_size = "11-40M"
        industry = "Upstream - on water"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

#---------41-100M$ projects-------------

    elif user_input_size == "3" and user_input_industry == "1":
        total = 0
        project_size = "41-100M"
        industry = "Refining"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "3" and user_input_industry == "2":
        total = 0
        project_size = "41-100M"
        industry = "Chemicals"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "3" and user_input_industry == "3":
        total = 0
        project_size = "41-100M"
        industry = "Upstream - on land"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "3" and user_input_industry == "4":
        total = 0
        project_size = "41-100M"
        industry = "Upstream - on water"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

#---------101-500M$ projects-------------

    elif user_input_size == "4" and user_input_industry == "1":
        total = 0
        project_size = "101-500M"
        industry = "Refining"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "4" and user_input_industry == "2":
        total = 0
        project_size = "101-500M"
        industry = "Chemicals"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "4" and user_input_industry == "3":
        total = 0
        project_size = "101-500M"
        industry = "Upstream - on land"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "4" and user_input_industry == "4":
        total = 0
        project_size = "101-500M"
        industry = "Upstream - on water"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")


#--------->500M$ projects-------------

    elif user_input_size == "5" and user_input_industry == "1":
        total = 0
        project_size = ">500M"
        industry = "Refining"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "5" and user_input_industry == "2":
        total = 0
        project_size = ">500M"
        industry = "Chemicals"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "5" and user_input_industry == "3":
        total = 0
        project_size = ">500M"
        industry = "Upstream - on land"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    elif user_input_size == "5" and user_input_industry == "4":
        total = 0
        project_size = ">500M"
        industry = "Upstream - on water"
        for position in positions:
            total += position.get_schedule_cost(project_size)*position.ind_multiplier(industry)
        print(f"Resource planning costs are approximately {round(total, -4)}$. Duration and personnel assumptions below:")

    else:
        print("Please enter a number 1-5")

#---------------------user_input_size assumptions-----------------
    if user_input_size == "1":
        print("""0-10M$ project assumes 8 month development duration to investment decision and the following personnel (can adjust, if known): 
    Full-time - Designer (1) 
    Part-time - Business Contact (0.1), Design Lead (0.2), PE (0.2), CM (0.1), Procurement Advisor (0.1), Cost Eng (0.2), Contracts Eng (0.1)
""")

    if user_input_size == "2":
        print("""11-40M$ project assumes 11 month development duration to investment decision and the following personnel (can adjust, if known): 
    Full-time - Designer (1)
    Part-time - Business Contact (0.2), Design Lead (0.3), PE (0.4), CM (0.15), Procurement Advisor (0.15), Cost Eng (0.3), Cost Lead (0.1), Contracts Eng (0.2), Project Controls Eng (0.1), Contracts Eng (0.1)
""")

    if user_input_size == "3":
        print("""41-100M$ project assumes 14 month development duration to investment decision and the following personnel (can adjust, if known): 
    Full-time - Project Manager - Development (1), Designer (1)
    Part-time - Business Contact (0.3), Design Lead (0.2), PE (0.5), CM (0.2), Procurement Advisor (0.2), Cost Eng (0.4), Cost Lead (0.1), Contracts Eng (0.25), Project Controls Eng (0.15), Schedule Eng (0.1), TBD (0.5)
""")

    if user_input_size == "4":
        print("""101-500M$ project assumes 17 month development duration to investment decision and the following personnel (can adjust, if known): 
    Full-time - Project Manager - Development (1), Design Lead (1), Designer (3), Project Eng (1), Cost Eng (1), TBD (2)
    Part-time - Business Contact (0.3), CM (0.25), Procurement Advisor (0.4), Procurement Manager (0.1), BSM (0.25), Cost Lead (0.2), Contracts Eng (0.3), Project Controls Eng (0.2), Schedule Eng (0.25), Project Manager - Execution (0.2)
""")

    if user_input_size == "5":
        print(""">500M$ project assumes 20 month development duration to investment decision and the following personnel (can adjust, if known): 
    Full-time - Business Service Manager (1), Project Manager - Development (1), Design Lead (1), Designer (5), Project Engineer (2), Cost Lead (1), Cost Eng (3), Schedule Eng (1), TBD (5)
    Part-time - Business Contact (0.4), CM (0.5), Procurement Advisor (0.5), Procurement Manager (0.15), Contracts Eng (0.5), Project Controls Eng (0.4), Project Controls Manager (0.1), Project Manager - Execution (0.3)
""")

#---------------------user_input_size assumptions-----------------

    if user_input_industry == "1":
        print("Refining projects are base case for this tool based on abundance of historical data available, so multiplier is 1.0")

    if user_input_industry == "2":
        print("Chemicals projects are more complex than refining and typically cost ~10% more, so multiplier is 1.1")

    if user_input_industry == "3":
        print("Upstream - land projects require unique skillsets that cost more and require remote travel, so multiplier is 1.3")

    if user_input_industry == "4":
        print("Upstream - on water projects require unique skillsets/studies that cost more and require remote travel, so multiplier is 1.4")



# total = 0
# project_size = "101-500M"
# for position in positions:
#     total += position.get_schedule_cost(project_size)
# print(round(int(total))) #want to round to nearest 10,000



positions = [
    Position("Project Manager - Development", 11000,{
        "0-10M": 0,
        "11-40M": 0,
        "41-100M": 1,
        "101-500M": 1,
        ">500M": 1,
    }), 
    Position("Design Lead", 10000,{
        "0-10M": 0.2,
        "11-40M": 0.2,
        "41-100M": 0.3,
        "101-500M": 1,
        ">500M": 1,
    }),
    Position("Designer", 9000,{
        "0-10M": 1,
        "11-40M": 1,
        "41-100M": 1,
        "101-500M": 3,
        ">500M": 5,
    }),
    Position("Business contact", 9500,{
        "0-10M": 0.1,
        "11-40M": 0.2,
        "41-100M": 0.3,
        "101-500M": 0.3,
        ">500M": 0.5,
    }),
    Position("Project Manager - Execution", 11000,{
        "0-10M": 0,
        "11-40M": 0,
        "41-100M": 0,
        "101-500M": 0.2,
        ">500M": 0.3,
    }),
    Position("Project Engineer", 9000,{
        "0-10M": 0.2,
        "11-40M": 0.3,
        "41-100M": 0.5,
        "101-500M": 1,
        ">500M": 2,
    }),
    Position("Construction Manager", 10000,{
        "0-10M": 0.1,
        "11-40M": 0.1,
        "41-100M": 0.2,
        "101-500M": 0.25,
        ">500M": 0.5,
    }),
    Position("Cost Lead", 9000,{
        "0-10M": 0,
        "11-40M": 0.1,
        "41-100M": 0.2,
        "101-500M": 0.5,
        ">500M": 1,
    }),
    Position("Cost Engineer", 7500,{
        "0-10M": 0.2,
        "11-40M": 0.3,
        "41-100M": 0.5,
        "101-500M": 1.5,
        ">500M": 3,
    }),
    Position("Schedule Engineer", 8000,{
        "0-10M": 0,
        "11-40M": 0.1,
        "41-100M": 0.3,
        "101-500M": 1,
        ">500M": 2,
    }), 
    Position("Procurement Manager", 9000,{
        "0-10M": 0,
        "11-40M": 0,
        "41-100M": 0.1,
        "101-500M": 0.15,
        ">500M": 0.25,
    }), 
    Position("Procurement Advisor", 8000,{
        "0-10M": 0,
        "11-40M": 0.05,
        "41-100M": 0.2,
        "101-500M": 0.3,
        ">500M": 0.4,
    }),  
    Position("Business Service Manager", 11000,{
        "0-10M": 0,
        "11-40M": 0,
        "41-100M": 0,
        "101-500M": 0.25,
        ">500M": 1,
    }), 
    Position("Project Controls Manager", 10000,{
        "0-10M": 0,
        "11-40M": 0,
        "41-100M": 0,
        "101-500M": 0.1,
        ">500M": 0.25,
    }),   
    Position("Project Controls Engineer", 8000,{
        "0-10M": 0,
        "11-40M": 0.1,
        "41-100M": 0.15,
        "101-500M": 0.2,
        ">500M": 0.4,
    }),  
    Position("Contracts Engineer", 8000,{
        "0-10M": 0,
        "11-40M": 0.1,
        "41-100M": 0.2,
        "101-500M": 0.3,
        ">500M": 0.5,
    }),    
    Position("TBD", 8000,{
        "0-10M": 0,
        "11-40M": 0.5,
        "41-100M": 1,
        "101-500M": 3,
        ">500M": 5,
    }),        
] 

main()