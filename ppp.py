# 从ryu的库里面导入各种函数文档
from ryu.app import simple_switch_13
from ryu.controller.handler import set_ev_cls
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER,DEAD_DISPATCHER



class MyMonitor(simple_switch_13):    #simple_switch_13 is same as the last experiment which named self_learn_switch
    '''
    design a class to achvie managing the quantity of flow
    '''

    def __init__(self,*args,**kwargs):
        super(MyMonitor,self).__init__(*args,**kwargs)

    @set_ev_cls(ofp_event.EventOFPStateChange,[MAIN_DISPATCHER,DEAD_DISPATCHER])
    def _state_change_handler(self,ev):
        '''
        design a handler to get switch state transition condition
        '''
        pass

    def _monitor(self):
        '''
        design a monitor on timing system to request switch infomations about port and flow
        '''
        pass

    def _request_stats(self,datapath):
        '''
        the function is to send requery to datapath
        '''
        pass

    @set_ev_cls(ofp_event.EventOFPPortStatsReply,MAIN_DISPATCHER)
    def _port_stats_reply_handler(self,ev):
        '''
        monitor to require the port state, then this function is to get infomation for port`s info
        '''
        pass

    @set_ev_cls(ofp_event.EventOFPFlowStatsReply,MAIN_DISPATCHER)
    def _port_stats_reply_handler(self,ev):
        '''
        monitor to require the flow state, then this function is to get infomation for flow`s info
        '''
        pass
