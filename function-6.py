def generate_tuples(end_value):
    """generate a list of tuples(x,x*2,x*3) for x from 1 to end_value(inclusive)."""
    return[(x,x*2,x*3) for x in range(1, end_value+1)]

end=5
result=generate_tuples(end)
print(result)
