'''planet1 = "Closest to sun"
print(planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])

print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

# Slicing a string

print(planet1[1:4])
print(planet1[:])
print(planet1[:7])
print(planet1[11:])

# Slicing a tuple

devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print(devops[0])
print(devops[4])
print(devops[-1])

print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])

# List

devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
print(devops[0])
print(devops[4])
print(devops[-1])

print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])
'''

# Dictionary example


Skill = {"DevOps":("AWS", "Jenkins", "Python", "Ansible"), "Development":["Java", "NodeJS", ".net"]}

print(Skill)
print(Skill["DevOps"])
print(Skill["Development"])

print(Skill["DevOps"][-1])
print(Skill["DevOps"][-1][:3])

