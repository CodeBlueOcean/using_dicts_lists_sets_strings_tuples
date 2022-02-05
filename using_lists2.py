states = ["Washington", "Oregon", "California"]

for x in states:
    state = state.lower()
    print(states)

"""
print(states[-1])
print(states[-2])
print(states[-3])
"""
print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)

states2 = ["Arizona", "Ohio", "Louisiana"]
best_states = states + states2
print(best_states)
print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])

# print(states)
# print(len(states))

# listname.methodname(arguments)
# states.append("New York")
states.append("New York")
print(states)
states.pop()
print(states)
states.pop(1)
print(states)




  