## Assignment
Complete the `Member`, `Student`, `Instructor` and `Workshop` classes in `dojo.py`.
In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a child of Rectangle and inherit methods and property.

### Member class

You're starting your own coder dojo! Everybody at
Codebar - whether they are attending workshops or teaching them - is
a Member and should be initialised with a `full name`. Which in the class is split into the properties `first name` and `last name` The class should contain the following methods:
* `introduce()`: returns a string with an introduction  (e.g., "Hi, my name is Marc!").
* `description()`: returns a string with the reason or bio (see ahead) (e.g., "I've always wanted to make websites"). This function should return without any value.

### Student and Instructor class

Each Member is also either a Student or an Instructor.
 
A Student has a `reason` for coming to the dojo. (e.g., "I've always wanted to make websites!"). They also have a lists of `interests`(e.g., `["C#", "Paskal", "Java"]`), which should be empty by default. The Student class has two additional methods:
*  `add_interest()`: Add an interest to the `interests` property. If the interest is already present it should instead print a message stating the student is already interested.
*  `remove_interest()`: Add an interest to the `interests` property. If there is no interest present it should instead print a message stating the student was never interested.

Each Instructor has a `bio` (e.g., "I've been coding in Python for 5 years!"). Furthermore they all have a list of `skills` (e.g., `["Python", "Javascript", "C++"]`), which should be empty by default. The Instructor class has one additional method:
*  `add_skill()`: Add a skill to the `skills` property. If the interest is already present it should instead print a message stating the instructor already had that skill.

Also fill in the `description()` method, already defined in Member, for both these classes. In the case of Student with `reason`, in the case of Instructor with `bio`.

### Workshop class

Your dojo consists of Workshops. Each Workshop has:

* A `date`.
* A `subject`.
* A list of `instructors`. Starts empty
* A list of `students`. Starts empty
* An `add_participant()` method that accepts a member as an argument. If the Member is an Instructor, add them to the instructors list. If a Member is a Student, add them to the students list. However, this should only happen if the `subject` of a workshop matches their `interests` or `skills`. In case it doesn't. This method should instead print a message stating that this person is either not interested or not skilled in this workshops subject. It also shouldn't add members who are already part of the workshop. In this case it should print a message stating that this person is already attending.
* An `update()` method that removes students from this workshop if their interests no longer align with it. It should print which members left.
* Printing the object should give the details of this workshop (see Usage example).

### Usage example

Here is an example of the output: for `print(workshop_HTML)`
```
Workshop - 12/03/2014 - HTML

Total attendees: 4

Students
 1. Jane Doe - Python, HTML,
    I am trying to learn programming and need some help
 2. Lena Smith - HTML, C#,
    I am really excited about learning to program!

Instructors
 1. Vicky Ruby - HTML, JavaScript,
    I want to help people learn coding.
 2. Nicole McMillan - HTML, Ruby,
    I have been programming for 5 years in Ruby and want to spread the love

```

#### Implementation

You can test dojo.py using the examples given in `test.py`. Afterwards in `main.py` add the following members:
* `jan` : Full name Jan Hancock. Is trying to learn programming but needs help. Interests are Python, C++, HTML.
* `piet` : Full name Piet Pieters. Is really excited to learn programming. Interests are C, R, Java.
* `joris`: Full name Joris Engelen. Wants to help people learn programming. Skills are Python, C#, R.
* `korneel`: Full name Korneel Kaneel. Has been programming for 5 years. No skills at present

Also make the following workshops:
* `workshop_1` : Planned on 03/05/2022. Subject is Python.
* `workshop_2` : Planned on 08/06/2022. Subject is C#.

Print the introduction of `Joris` and the description of `Piet`. The code should return:
```
Hi, my name is Joris!
I am really excited to learn programming.
```

Try adding all members to each workshop. Afterwards print the details of both workshops. This should return:
```
Piet is not interested in this workshop
Korneel is not skilled enough to give this workshop

Workshop - 03/05/2022 - Python

Total attendees: 2

Students
 1. Jan Hancock - Python, C++, HTML,
    I am trying to learn programming and need some help

Instructors
 1. Joris Engelen - Python, C#, R,
    I want to help people learn coding.


Jan is not interested in this workshop
Piet is not interested in this workshop
Korneel is not skilled enough to give this workshop

Workshop - 08/06/2022 - C#

Total attendees: 1

Students

Instructors
 1. Joris Engelen - Python, C#, R,
    I want to help people learn coding.

```

Remove/Add the following interests and skills:
* `jan` : Remove Python and C#
* `piet` : Add HTML and Python
* `joris`: Add HTML and Javascript
* `korneel`: Add Python

Update workshop_1. Afterwards, once again try adding everyone to the workshop_1 and print workshop_1:
```
Jan was not interested in C#
Piet is already interested in HTML

Jan will no longer attend this workshop
Jan is not interested in this workshop
Joris is already attending this course

Workshop - 03/05/2022 - Python

Total attendees: 3

Students
 1. Piet Pieters - C, R, HTML, Python,
    I am really excited about learning to program!

Instructors
 1. Joris Engelen - Python, C#, R, HTML, JavaScript,
    I want to help people learn coding.
 2. Korneel Kaneel - Python,
    I have been programming for 5 years in Python
```

### Extra
The current way of adding people to workshops is annoying. Design a class called `Member_list`. As a property it should have a list with all the members of the dojo (See 1.3.5 nesten van objecten). It has the following methods:
* `add_member` : Add a member to the Member_list object.
* `remove_member` : Remove a member from the Member_list object.

The update `update()` method of the class Workshop needs to accept an object of Member_list and update that workshop based on the interests and skills of the members on this list.

