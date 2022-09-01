it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies));
it_companies.add('Twitter');
print(len(it_companies));
update_set=['X','Y','Z'];
it_companies.update(update_set);
print(len(it_companies));
it_companies.remove('Z');
print(len(it_companies));

# The built-in method, remove() in Python,
# removes the element from the set only if the element is present in the set,
# just as the discard() method does but If the element is not present in the set,
# then an error or exception is raised.

Join = A.union(B)
print(Join);
print(A.intersection(B));
print(A.issubset(B));
print(A.isdisjoint(B))
AB = A.union(B)
print(AB);
BA = B.union(A)
print(BA);
s = A.symmetric_difference(B)

print(s);