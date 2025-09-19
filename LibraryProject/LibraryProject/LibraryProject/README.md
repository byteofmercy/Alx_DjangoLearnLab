# \# Permissions and Groups Setup

# 

# \## Custom Permissions

# In `bookshelf/models.py`, we added:

# \- can\_view

# \- can\_create

# \- can\_edit

# \- can\_delete

# 

# \## Groups

# We created groups via Django admin:

# \- \*\*Viewers\*\* → can\_view

# \- \*\*Editors\*\* → can\_view, can\_create, can\_edit

# \- \*\*Admins\*\* → can\_view, can\_create, can\_edit, can\_delete

# 

# \## Views Protection

# In `bookshelf/views.py`, we used `@permission\_required` to protect:

# \- book\_list → needs can\_view

# \- book\_create → needs can\_create

# \- book\_edit → needs can\_edit

# \- book\_delete → needs can\_delete

# 

# Assign users to groups in admin to control access.



