An array was used to store the list of users and group since to perform iteration. A list is also used to check for groups already checked to avoid cyclic relationships. It is achieved through recursion

Time complexity- O(n^2) since the recursion happens every time a group is encountered. n is the length of the sub_group

Space complexity - O(nm) where n is the depth of the recursion, m is the space occupied by each recursive call in the memory
