# Sorting 

# sort method :
    # 1. sort method can be used for sorting but it changes the list. 
    # 2. It cannot sort tuples


# sorted method
    # 1. It does not change the original list
    # 2. It can sort tuples 


earth_metals = ["Berrylium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]

earth_metals.sort()

print(earth_metals)

# Reverse sorting

earth_metals.sort(reverse = True)

print(earth_metals)

# Sorting tuple using sort function--> Not possible as tuples are immutable !! 

# tuple example

earth_metals = ("Berrylium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")   

# sorted function can do the job !!!

earth_metals = ("Berrylium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")

sorted_earth_metals = sorted(earth_metals)

print(sorted_earth_metals)
