'''
################################################
#  Program: Pod_members.py                     #
#  Author: Baba                                #
#  Date: 2/17/2021                             #
#  Description: Program to be used by the      #
#               POD members in instructing     #
#               the POD members about Object   #
#               Oriented Programming concepts  #
#  The Hidden Genius Project                   #
#  OAK8 Cohort                                 #
################################################
'''

class Pod_members:
  
    # Class Constructor method is called when an Object is instantiated
    def __init__(self, pod_member):
       self.pod_member = {}

    # Class method to add a member to the pod_leader dictionary       
    def add_member(self, member_to_add,cell_number):
        self.pod_member[member_to_add] = cell_number
        
    # Class method to print the pod_member and cell numbers   
    def display_members(self):
      print('POD members')      
      for member, number in self.pod_member.items():
        print(member, number)
            
pod = Pod_members("POD members");
pod.add_member("Richard","(510) 228-5623")
pod.add_member("kymari","(510)575-1982")
pod.add_member("gaelen","(510)816-2411")
pod.add_member("myles","(510)500-7266 ")
pod.display_members()
