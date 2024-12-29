# Dungeon First Search

## Description
This is a child of another one of repo's, Kingdom of N-Grams. That project is a text adventure game made modular by data stored locally in a .json file. This program checks if the room_data.json file is viable as a map for the game. It uses a depth first search algorithm to check if there is an ending for the user to reach based on a customizable map.

## Additional Information
room_data.json is a nested dictionary with the room name being the key, and the nested dicitonary being initialized as "exits" and the final dictionary value is the possible exit room names.

## Formatting and tests
### There is an end because an "end room" exists and is possible to reach
```
"start" : {
  "exits" : {
    "north" : "room to the north",
    "east" : "room to the east",
    "south" : "end"
    }
},
"end" : {
  "exits" : {
  }
}
```

### There is no end because although an "end room" exists, but there is no possible exit
```
"start" : {
  "exits" : {
    "north" : "room to the north"
    }
},
"room to the north" : {
  "exits" : {
    "east" : "room to the east"
    }
  }
"end" : {
  "exits" :{
  }
}
```
