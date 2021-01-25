class Position:
    def __init__(self, title, salary, fte_values):
        self.title = title
        self.salary = salary
        self.fte_values = fte_values

    def get_schedule_cost(self, size):
        months = {
            "0-10M" : 8, 
            "11-40M" : 11,
            "41-100M" : 14, 
            "101-500M" : 17,
            ">500M" : 20
        }
        return self.salary*self.fte_values[size]*months[size]

    def ind_multiplier(self, industry):
        multiplier = {
            "Refining" : 1,
            "Chemicals" : 1.1,
            "Upstream - on land" : 1.3,
            "Upstream - on water" : 1.4,
        }
        return multiplier[industry]        


# class PM(Position):