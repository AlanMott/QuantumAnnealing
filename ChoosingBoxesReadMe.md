Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@AlanMott 
dwave-training
/
choosing-boxes
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
You’re making changes in a project you don’t have write access to. We’ve created a fork of this project for you to commit your proposed changes to. Submitting a change will write it to a new branch in your fork, so you can send a pull request.
choosing-boxes
/
README.md
in
dwave-training:master
 

Spaces

2

Soft wrap
1
# Choosing Boxes
2
​
3
You're given three boxes with values 17, 21, and 19.
4
​
5
Write a BQM and an Ocean program that returns the pair of boxes with the
6
smallest sum.  A starter file has been provided for you in
7
``choosing_boxes.py``.
8
​
9
**Remember:**
10
​
11
You will need to choose a value for your Lagrange parameter and number of QPU
12
reads.  The autograder will test if your Lagrange parameter is large enough
13
that the desired solution (boxes 17 and 19) has the smallest value.
14
​
15
*For students in class submitting to our autograder:*
16
​
17
Please index boxes 17, 21, and 19, using the string names 'box_17', 'box_19',
18
and 'box_21', respectively, in your BQM.  For example, if the coefficient on
19
the linear term for Box 17 is 5, your program might set
20
`bqm.set_linear('box_17', 5)`.
21
​
22
## Instructions
23
​
24
To write your program, please complete the following in `choosing_boxes.py`:
25
​
26
- Add your token to the ``get_token`` function.
27
- Build your BQM in the ``get_bqm`` function, and set the Lagrange parameter.
28
- Find a good value ``numruns`` in the ``run_on_qpu`` function
29
- Complete the main function (bottom of the file) by defining a sampler,
30
  running your problem on that sampler, and looking at the results.  "Looking
31
at the results" may be as simple as printing out the sampleset object - it's up
32
to you!
33
​
34
## License
35
​
36
Released under the Apache License 2.0. See [LICENSE](LICENSE) file.
37
​
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
@AlanMott
Propose changes
Commit summary
Create README.md
Optional extended description
Add an optional extended description…
 
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
You have no unread notifications
