sisters = ('A', 'B','C')
brothers = ('X','Y','Z')


siblings = sisters + brothers

print("The tuple after concatenation is : " )

siblings = siblings + ('Father',)
siblings = siblings + ('Mother',)
print(siblings)

print(len(siblings))

# Empty tuple
family_members = ()

family_members= siblings
print(family_members)