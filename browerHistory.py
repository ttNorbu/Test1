from queue import LifoQueue

backward_History = LifoQueue()
forward_History = LifoQueue()
curent_page = None
# visit function
Noofvisits = int(input("Enter the number of url history:\n"))
print("Enter URLs to visit:\n")
for i in range(Noofvisits):
    url = input("URL: ")
    print(f"Visiting {url}")
    backward_History.put(current_page)
    current_page = url

# display
print(f"current page: {current_page}")

# Go back
while input(" Do you want to go back? (Yes/No): ").lower() == 'Yes':
    if not backward_History.empty():
        forward_History.put(current_page)
        current_page = backward_History.get()
        print(f" Going back to {current_page}")
    else:
        print("No previous page available")

# Go forward

while input(" Do you want to go back? (Yes/No):").lower() == 'Yes':
    if not forward_History.empty():
        backward_History.put(current_page)
        current_page = forward_History.get()
        print(f" Going back to {current_page}")
    else:
        print("Forwards  page available")
    
