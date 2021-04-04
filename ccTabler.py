#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:46:00 2021

@author: catcry

catcry Table Class to draw a sophisticated table!

"""


class Tab_cc():
    def __init__(self,field_names,column_lenthes = None):
        
        self.no_cols=len(column_lenthes)
        self.lens=column_lenthes
        self.fields = field_names
        self.table = ''
        
        def add_line(self,obj):
            if obj=='table':
                for col in range(self.no_cols):
                    self.table = self.table+'+'+'-'*self.lens[col]
                self.table=self.table+"+\n"
            elif obj=='row':
                for col in range(self.no_cols):
                    self.row = self.row+'+'+'-'*self.lens[col]
                self.row=self.row+"+\n"
        add_line(self,'table')
        for col in range(self.no_cols):
            self.table=self.table+'|'+self.fields[col]+' '*(self.lens[col]-len(self.fields[col]))
        self.table=self.table+'|\n'
        add_line(self,'table')
    
    def add_line(self,obj):
            if obj=='table':
                for col in range(self.no_cols):
                    self.table = self.table+'+'+'-'*self.lens[col]
                self.table=self.table+"+\n"
            elif obj=='row':
                for col in range(self.no_cols):
                    self.row = self.row+'+'+'-'*self.lens[col]
                self.row=self.row+"+\n"
            
           
    def add_row(self,context):
        self.context = context
    
        self.row=''
        for col in range(self.no_cols):
            self.row=self.row+'|'+self.context[col]+' '*(self.lens[col]-len(self.context[col]))
        self.row = self.row+"|\n"
        self.add_line('row')
        self.table = self.table + self.row
        return (self.row)
        
    
    def add_title(self,title):
        
        # self.add_line('row')
        spaces = (sum(self.lens) - len(title))//2
        self.row = '|'+' ' * spaces +title + ' '* (sum(self.lens)-spaces-len(title)+self.no_cols-1)+'|'
        
        self.row = self.row+"\n"
        self.add_line('row')
        self.table = self.table + self.row 
               
        return (self.row)



def amir(name,length =)