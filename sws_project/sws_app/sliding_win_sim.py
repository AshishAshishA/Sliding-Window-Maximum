from collections import deque

class sliding_win:

    def __init__(self,window_size):
        assert window_size>0 , f"window size : {window_size} should be greater than 0"
        self.list=[]
        self.result=[]

        self.popped_left=None
        self.popped_right=[]

        self.dq=deque()
        self.window_size=window_size
        self.index=-1

    def update_list(self,num:int):
        self.popped_left=None
        self.popped_right.clear()
        self.list.append(num)
        self.index+=1

        if self.index>=self.window_size:
            return True
        else:
            return False


    def sliding_win_func(self):
        
        if len(self.dq)!=0 and self.dq[0]==self.index-self.window_size:
            self.popped_left=self.dq[0]
            self.dq.popleft()
        
        while len(self.dq)!=0 and self.list[self.dq[-1]]<self.list[self.index]:
            self.popped_right.append(self.dq[-1])
            self.dq.pop()

        self.dq.append(self.index)

        if self.index-self.window_size+1>=0 :
            self.result.append(self.list[self.dq[0]])

        return self.result

    def update_list_and_result(self,num:int):
        self.update_list(num)
        # if self.index>=self.window_size:
        self.sliding_win_func()

    
if __name__=='__main__':
    sw1=sliding_win(3)

    sw1.update_list_and_result(1)
    sw1.update_list_and_result(3)
    sw1.update_list_and_result(-1)
    sw1.update_list_and_result(-3)
    sw1.update_list_and_result(5)
    sw1.update_list_and_result(3)
    sw1.update_list_and_result(6)
    sw1.update_list_and_result(7)

    for i in sw1.list:
        print(i)
    print()

    if len(sw1.list)>=sw1.window_size:
        res=sw1.result

        for i in res:
            print(i)

    else:
        print("requires not elements at least equal to window size")

    

        

