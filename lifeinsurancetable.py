import scipy
import streamlit as st

# from txt_to_list import convert_to_table

def convert_to_table(filename:str):
    table = []
    with open(filename) as file:
        lines = file.readlines()
        # for line in lines
        for line in lines:
            linelist = line.split()
            table.append(float(linelist[-4]+linelist[-3]+linelist[-2]))
    
    return table
    



class Lifetable:
    
    def __init__(self,table,start_year):
        self.start = start_year
        self.table = table
        self.max = start_year+len(self.table)-1

    def survive(self,initial,period):
        if initial+period>self.max:
            raise ValueError("Age is too large")
        res = self.table[initial+period-self.start]/self.table[initial-self.start]
        return res
    
    def deferred_death(self,initial,defer,period):
        survival_prob = self.survive(initial,defer)
        death = 1- self.survive(initial+defer,period)
        return survival_prob *death
    
    def assurance_EV(self,interest,start,end=None,select = False):
        if select == True:
            raise ValueError("Not implemented yet.")
        if end == None:
            end = len(self.table) + self.start -1
            # raise ValueError("Not implmented yet")
        if end>=len(self.table) + self.start :
            raise ValueError("Age is Too large (Assurance_EV)")
        # start_index = 

        temp_count = 0
        res = 0
        for i in range(start,end):
            prob = self.deferred_death(start,i-start,1)
            value = 1/((1+interest)**(i-start+1))
            res += prob * value
            temp_count += 1
        # print(f'Added {temp_count} times')
        
        
        
        return res




        
    #     #Whole life assurance
    #     if end is None:
        
        
    #     else:


    
# def compute_discrete_annuity_EV(lifetable,interest_rate):

#     scipy.

if __name__ == "__main__":
    table = convert_to_table("lifetable.txt")
    print(table)
    lifetable = Lifetable(table,17)
    print(len(lifetable.table))
    print(lifetable.max)
    res2 = lifetable.survive(72,45)
    print(res2)


    res3 = lifetable.assurance_EV(0.04,50,52)

    # res4 = lifetable.assurance_EV(0.04,50,117)
    res4 = lifetable.assurance_EV(0.04,50,)
    res5 = lifetable.assurance_EV(0.04,52,117)
    print(res3)
    print(res4)
    print(res5)
