class txteditor:
  def __init__(self):
    self.text = ""
    self.undo_stack = []
    self.redo_stack = []

  def texttake(self, newtext):
    self.undo_stack.append(self.text)
    self.text += f"{newtext} "
    self.redo_stack.clear()

  def undo(self):
    if self.undo_stack:
      self.redo_stack.append(self.text)
      self.text = self.undo_stack.pop()

  def redo(self):
    if self.redo_stack:
      self.undo_stack.append(self.text)
      self.text = self.redo_stack.pop()

  def display(self):
    print(f"\nCurrrent text: {self.text}\n")


system = txteditor()

print("----Undo-Redo System----")
choice = 0
while choice != 5:
  try:
    print("\n1: Adding text\n2: Undo\n3: Redo\n4: Display\n5: Exit")
    choice = int(input("Enter your choice: "))
  except(ValueError):
    print("Wrong value entered, Try again")
    continue
  match (choice):
  
    
    case 1:
      
      addtext = input("\nEnter what you want to add: ")
      system.texttake(addtext)
        # wrong logic
        # print("1: Adding text\n2: Undo\n3: Redo\n4: Display\n5: Exit")
        # choice = int(input("Enter your choice: "))
      
        
      
      
    case 2: 
      system.undo()
    case 3:
      system.redo()
    case 4:
      system.display()
    case 5:
      print("\nExit Succesfully")
      
      