# -*- coding: utf-8 -*-
"""
Created on Feb 02nd, 2018
Source for implementing the environment (and consequently task to be solved).
@author: Felipe Leno
"""

import random
import math



class Environment:
    
    def get_state(self):
        """**Implement Here***
            How to read the current state
        """
        #TODO: Implement how to get the real state
        return (1,5)
    def step(self,action):
        """**Implement Here***
            The state transition. The agent executed the action in the parameter
        """
        #The return is the next state, the action executed, and the reward
        #TODO: Implement Here the state transition
        statePrime = self.get_state() #Get next State
        #TODO: Implement the real reward
        reward = random.random()

        return statePrime,action,reward