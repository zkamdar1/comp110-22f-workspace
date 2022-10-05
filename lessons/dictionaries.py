"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
from operator import is_


schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set the key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Acccess a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary by its key
schools.pop("Duke")


# Test for existence of a key
is_duke_present: bool = "Duke" in schools
print(f"is_duke_present: {is_duke_present}")

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {} # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")