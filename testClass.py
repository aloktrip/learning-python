class Program():
  def __init__(self, *args, **kwargs):

    self.lang = input("What Language: ")
    self.version = float(input("Version?: "))
    self.skill = input("Skill Level : ")
p1 = Program()
print(p1.lang)
print(p1.version)
