from django.shortcuts import render
from enum import Enum
from .sliding_win_sim import sliding_win

obj=None

def obj_creator(window_size:int):
    global obj
    obj=sliding_win(window_size)

# Create your views here.
def get_index(request):
    if request.method=="POST":

        window_size=int(request.POST.get('window_size'))

        obj_creator(window_size)

        return render(request,'sws_app/sw_maxi.html',{"window_size":window_size})
    return render(request,'sws_app/index.html',{})

def sw_simulator(request):
    if request.method=="POST":

        num=int(request.POST.get('num'))
        
        obj.update_list_and_result(num)
        obj_list=list(enumerate(obj.list))

        dq=obj.dq

        dq_list = list()
        for ele in dq:
            dq_list.append(ele)

        res=list(enumerate(obj.result))
        popped_left=obj.popped_left
        popped_right=obj.popped_right
        window_size=obj.window_size

        print(window_size)
        
        context={
            "list":obj_list,
            "dq_list":dq_list,
            "res":res,
            "popped_left":popped_left,
            "popped_right":popped_right,
            "window_start":len(obj_list)-window_size,
            "curr_ind":len(obj_list)-1,
            "res_ind":len(res)-1,
            "window_size":window_size,
        }
        return render(request,'sws_app/sw_maxi.html',context)
    return render(request,'sws_app/index.html',{})
