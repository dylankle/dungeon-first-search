import json

# Get room data from user edited json
with open('rooms_data.json') as rooms_file:
    rooms_data = json.load(rooms_file)

# List for visited rooms
visited = ["start"]
# List implemented stack for current connected rooms
connected = []

# Starting room is selected as parent node
for exit in rooms_data["start"]["exits"]:
    visited.append(rooms_data["start"]["exits"][exit])
    connected.append(rooms_data["start"]["exits"][exit])

# Appending function for new top of stack
def adjacent_rooms(room):
    for exit in rooms_data[room]["exits"]:
        # If it has not been seen add to the connected list
        if rooms_data[room]["exits"][exit] not in visited:
            connected.append(rooms_data[room]["exits"][exit])
            visited.append(rooms_data[room]["exits"][exit])

# Begin DFS starting at room at the top of the stack
while len(connected) != 0:
    top = connected.pop()
    adjacent_rooms(top)

# Result print if a room named "end" was visited
if "end" in visited:
    print("There is an end")
else:
    print("There is no end")