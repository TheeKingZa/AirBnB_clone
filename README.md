AirBnB Clone - Command Interpreter
------------------------------------

Project Description
-------------------

This project is the first step in building your own version of Airbnb. You'll create a Python package that includes a command interpreter, allowing you to manage Airbnb-like objects. This initial step is crucial because it forms the foundation for future tasks like HTML/CSS templating, database storage, API development, and front-end integration.

Command Interpreter
What's a Command Interpreter?
Think of it as a special tool, similar to a magical wand, that lets you control your program. With the command interpreter, you can:

Create: Make new objects like users, states, cities, and places. It's like creating new things with building blocks.

Retrieve: Get information about objects from files or databases. It's like finding your favorite toy in a toy chest.

Do Operations: You can perform actions on objects, like counting them or calculating statistics. Imagine playing different games with your toys.

Update: Change attributes or properties of objects. It's like repainting your building blocks or adding new parts to your creations.

Destroy: Remove objects when you don't need them anymore. It's like taking apart what you've built.


How to Start the Command Interpreter
To start the command interpreter, follow these steps:

Make sure you have Python installed on your computer.

Clone this project from the repository.

Navigate to the project folder in your terminal or command prompt.

Run the command interpreter using the following command:

javascript
------------------------------------
==Code==

python3 console.py

This will launch the command interpreter, and you'll see a prompt where you can enter commands.

------------------------------------
How to Use the Command Interpreter
Once the command interpreter is running, you can enter commands. Here are some basic commands:
------------------------------------

create: Create a new object (e.g., user, state, city).

sql
------------------------------------
==Code==
create User
show: Retrieve information about an object.

------------------------------------
sql
------------------------------------
==Code==
show User 1234-5678
update: Update attributes of an object.

------------------------------------
sql
------------------------------------
==Code==
update Place 8765-4321 name "New Name"
destroy: Remove an object.

------------------------------------
yaml
------------------------------------
==Code==
destroy State 2468-1357
all: List all objects of a specific type.

------------------------------------
css
------------------------------------
==Code==
all City
quit or EOF: Exit the command interpreter.

------------------------------------
Examples
Here are some examples of how to use the command interpreter:
------------------------------------
Creating a new user:

sql
------------------------------------
==Code==
    create User
        Retrieving information about a place:
        
------------------------------------
sql
------------------------------------
==Code==
    show Place 1234-5678
        Updating the name of a city:
        
------------------------------------
sql
------------------------------------
==Code==
    update City 8765-4321 name "New York"
        Destroying a state:
        
------------------------------------
yaml
------------------------------------
==Code==
    destroy State 2468-1357

......................................................................
