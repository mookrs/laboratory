# Unpacking Elements from Iterables of Arbitrary Length
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

# Recursive
items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))
