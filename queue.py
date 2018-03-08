# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 10:33:27 2018

@author: onion
"""

class Queue():  
    def __init__(self,size):  
        self.size=size;  
        self.front=-1;  
        self.rear=-1;  
        self.queue=[];  

    def __str__(self):  #  输出队列
    #类的字符串输出方法
        return str(self.queue)

    def enqueue(self,ele):  #入队操作  
        if self.isfull():  
            raise exception("queue is full");  
        else:  
            self.queue.append(ele);  
            self.rear=self.rear+1;  
    def dequeue(self):      #出队操作  
        if self.isempty():  
            raise exception("queue is empty");  
        else:  
            self.front=self.front+1;  
            return self.queue[self.front];  
    def isfull(self):  
        return self.rear-self.front+1==self.size;  
    def isempty(self):  
        return self.front==self.rear;  
      
q=Queue(10);  
for i in [1,2,3,4,5]:  
    q.enqueue(i)  
print q
print q.dequeue()  
print q.isempty()
print q #输出队列