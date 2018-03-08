# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 11:03:41 2018

@author: onion
"""

#coding=utf-8
class Stack(object) :
  def __init__(self,size):
    #类的构造函数
    self.size = size
    self.stack = []

  def __str__(self):
    #类的字符串输出方法
    return str(self.stack)

  def getSize(self) :
    #获取栈当前大小
    return len(self.stack)

  def push(self, x) :
    #入栈，栈满抛异常
    if self.isfull() :
      #return -1
      raise Exception("Stack is full")
    self.stack.append(x)

  def pop(self) :
    #出栈，栈空抛异常
    if self.isempty() :
      #return -1
      raise Exception("Stack is empty")
    topElement = self.stack[-1] #非空的话输出最后一个元素
    self.stack.remove(topElement)
    return topElement

  def isempty(self) :
    #判断栈空
    if len(self.stack) == 0 :
      return True
    return False

  def isfull(self) :
    #判断栈满
    if len(self.stack) == self.size :
      return True
    return False
    
if __name__ == '__main__' :
  stackTest = Stack(20)
  for i in range(11) :
    stackTest.push(i)

  print stackTest.getSize()

  print stackTest.isempty()
  print stackTest.isfull()
  print stackTest
  for i in range(6) :
    stackTest.pop()

  print stackTest.getSize()
  print stackTest