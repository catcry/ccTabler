#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:46:00 2021

@author: catcry

catcry Table Class to draw a simple table. 
Hope to develop it into a sophisticated one!

"""


class Tab_cc():
    
    def add_line(self,obj):
            if obj=='table':
                for col in range(self.no_cols):
                    self.table = self.table+'+'+'-'*self.lens[col]
                self.table=self.table+"+\n"
            elif obj=='row':
                for col in range(self.no_cols):
                    self.row = self.row+'+'+'-'*self.lens[col]
                self.row=self.row+"+\n"
            
    def table_draw (self):
        self.table = ''
       
        self.add_line('table')
        
        for col in range(self.no_cols):
            self.table = self.table + '|'+self.fields[col]+' '*(self.lens[col]-len(self.fields[col]))
            
        self.table=self.table + '|\n'
        self.add_line('table')      
        if self.content_stack:
            for row in self.content_stack:
                self.add_row(row,1)
        return self.table
    
    def __init__(self,fields_name,column_lengthes = None):
        self.rows = []
        self.no_cols=len(fields_name)
        if column_lengthes: 
            self.lens=column_lengthes
        else :
            lens = []
            for field in fields_name:
                lens.append(len(field))
            self.lens = lens
        self.fields = fields_name
        self.table = ''
        self.content_stack = []


        self.table_draw() 


           
    def add_row(self,content,redraw_flag = 0):
        
        if not redraw_flag:
            self.content_stack.append(content)
        self.row = ''
        redraw_flag = 0
        for col in range(self.no_cols):
            if len(content[col]) > self.lens[col]:
                redraw_flag = 1
                self.lens[col] = len(content[col])
            # the_row = the_row + '|'+self.content[col]+' '*(self.lens[col]-len(self.content[col]))
            self.row = self.row+'|'+content[col]+' '*(self.lens[col]-len(content[col]))
        # self.row_stack.append(the_row)
        
            
        self.row = self.row + "|\n"
        self.add_line('row')
        self.table = self.table + self.row
        if redraw_flag:
            self.table_draw()
        # return (self.row)
        
    
    def add_title(self,title):
        
        # self.add_line('row')
        spaces = (sum(self.lens) - len(title))//2
        self.row = '|'+' ' * spaces +title + ' '* (sum(self.lens)-spaces-len(title)+self.no_cols-1)+'|'
        
        self.row = self.row+"\n"
        self.add_line('row')
        self.table = self.table + self.row 
               
        return (self.row)

    def add_column (self, title, length = None):
        if not length:
            length = len(title)
        self.no_cols = self.no_cols + 1
        self.lens.append(length)
        self.fields.append(title)
        for row in self.content_stack:
            row.append('')
        self.table_draw()
    # def table_draw (self):
    #    self.table = ''
       
    #    self.add_line('table')
       
    #    for col in range(self.no_cols):
    #         self.table = self.table + '|'+self.fields[col]+' '*(self.lens[col]-len(self.fields[col]))
            
    #    self.table=self.table + '|\n'
    #    self.add_line('table')
       
    #    return self.table
