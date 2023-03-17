# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
old_min = -1
old_max = 1
new_min = 10
new_max = 90
old_value = old_min
for i in range (0,80):
    old_value= old_value+0.025
    new_value = ( ( float(old_value) - old_min ) / (old_max - old_min ) )* (new_max - new_min) + new_min
    print("New value:", new_value, "of old value", old_value)
