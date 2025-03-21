def sumaverage(marks):
    """calculate total and average of marks for 5 subject"""
    if len(marks) !=5:
        raise ValueError("exactly 5 marks must be provided.")

    total=sum(marks)
    average=total/len(marks)
    return total, average

marks=[85,90,81,92,89]
total,average=sumaverage(marks)

print(f"total marks:{total}")
print(f"average marks:{average}")
        
