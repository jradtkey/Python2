class Call(object):
    def __init__(self, call_id, name, phone, time, reason):
        self.call_id = call_id
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason

    def displayCall(self):
        print "Call ID: {}. Caller's name: {}. Phone number: {}. Time of call: {}. Reason for call: {}".format(self.call_id, self.name, self.phone, self.time, self.reason)
        return self

call1 = Call("1", "Bob", "6198514238", "4:45", "Refund")
call2 = Call("2", "Sue", "5558886262", "3:45", "Refund")
call3 = Call("3", "Dog", "6198514238", "2:45", "Customer Support")
#call1.displayCall()

class CallCenter(object):
    def __init__(self, call):
        self.queue = []
        self.queue_size = len(self.queue)

    def addCall(self, call):
        self.queue.append("CallID: "+ call.call_id +' ' + call.name + '-' + call.phone + '-' + call.time + '-' + call.reason)
        return self

    def removeCall(self):
        self.queue.remove(call_center.queue[0])
        return self

    def info(self):
        for call in self.queue:
            print call
        print len(call_center.queue)
        return self

call_center = CallCenter(call1)
call_center.addCall(call1)
call_center.addCall(call2)
call_center.addCall(call3)
call_center.removeCall()
call_center.info()

#print call_center.queue
#print len(call_center.queue)
