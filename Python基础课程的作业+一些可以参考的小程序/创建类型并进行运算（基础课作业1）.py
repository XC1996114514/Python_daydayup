class Human:
  def __init__(self,name='Anonymous',wallet=500):
    self.name = name
    self.wallet = wallet
  def hello(self):
    print("Hello! My name is ", self.name, ". I have ", self.wallet, 'JPY.')
  def give(self, p, money):
    """give money to other"""
    p.receive(money)
    self.wallet -= money
  def receive(self, money):
    """recieve money from other"""
    self.wallet += money

class Student(Human):
  def __init__(self,name='Anon. Student',wallet=500):
    ### write a method body to set additonal attributes ###
    self.subject = []
    super().__init__(name, wallet)

  def hello(self):
    super().hello()
    self.showclass()

  def learn(self,subject):
    subject = self.subject.append(subject)

  def showclass(self):
    print('My class =', self.subject)

  def teach(self, st):
    for sb in st.subject:
      if self.is_newsubj(sb):
        subject = self.subject.append(sb)
        self.wallet-=10
        st.wallet+=10

  def is_newsubj(self,sb):
    for s in self.subject:
      if sb ==s:
        return False
    return True




#
# Below is a test code. Expected result is:
# Hello! My name is  John . I have  500 JPY.
# I have learned: ['mathematics', 'history', 'biology', 'programming', 'statistics'] .
# Hello! My name is  Jack . I have  500 JPY.
# I have learned: ['programming', 'history', 'statistics', 'mathematics', 'biology'] .
#
john = Student("John")
john.learn('mathematics')
john.learn('history')
john.learn('biology') # mathematics, history, biology

jack = Student("Jack")
jack.learn('programming')
jack.learn('history')
jack.learn('statistics')

john.teach(jack)
jack.teach(john)

for p in (john,jack):
  p.hello()
