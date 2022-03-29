class clockTime:
  
  def __init__(self):
    hours = int(input("enter hours: "))
    self.sethours(hours)
    mins = int(input("enter mins: "))
    self.setminutes(mins)
    secs = int(input("enter seconds: "))
    self.setseconds(secs)
    self.setTime()
    self.showtime()

  def sethours(self, hours):
    self.hours = hours

  def setminutes(self, mins):
    self.mins = mins

  def setseconds(self, secs):
    self.seconds = secs

  def setTime(self):
    
    self.time = str(self.hours)+":"+str(self.mins)+":"+str(self.seconds)

  def showtime(self):
    print("time is set to: ", self.time)

clock = clockTime()
    
    