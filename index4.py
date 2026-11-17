# number=[10,20,30,40,50]
# names=["AN","DC","MC","AC"]
# combined_batch=number+names
# print(combined_batch)
# print(number)
# print(names)
# x=number.extend(names)
# print(x)
# print(number)
# print(names)

# ------------------------

# nums=[1,2,3]
# nums1=[5,6]
# nums.append(4)
# nums.extend(nums1)
# print(nums)

# ---------------------

# nums=[1,2,3]
# nums1=[5,6]
# nums.append(4)
# nums.append(nums1)
# nums.extend(nums1)
# print(nums)
# print(nums[4][0])

# ------------------------

# tupple

# dob=(22,8,2002)
# dob[0]=12
# print(dob)
# print(type(dob))

# a=(5)
# print(a)
# print(type(a))

# b=(5,)
# print(b)
# print(type(b))

# -----------------------

# tuple packing

# a=10,20,30
# print(a)
# print(type(a))
# print(a[1])
# print(a[-1])
# print(a[1:4])
# print(a[::-1])


# programming_language=("c","java","pyhton")
# print(programming_language)
# print(type(programming_language))
# print(programming_language[1])

# employee=("ashlin",19,"python developer")

# name=employee[0]
# age=employee[1]
# job_role=employee[2]
# print(name)
# print(age)
# print(job_role)


# name,age,job_role=employee
# name,age=employee,age
# print(name)
# print(age)
# print(job_role)

# name,age,job_role=employee
# print(name)
# print(age)
# print(job_role)

# print(name)
# print(*data)
# print(age)
# print(job_role)

# --------------------------

# tupple unpacking

# nums=(1,2,3,4,5,6,7,8)
# first,*middle,last=nums
# print(first)
# print(middle)
# print(last)

# -----------------------------

# tupple methods


# nums=(1,2,3,2,5,2,7,3)
# print(nums.count(2))
# print(nums.count(3))
# print(nums.count(7))
# print(nums.count(9))
# print(nums.index(2))

# -------------------------------


# Iteration


# nums=(1,2,3,2,5,2,7,3)
# for num in nums:
#     print(num)

# --------------------------------

# Iteration with index

# for i in range(len(nums)):
#     print(i,nums[i])

# ------------------------------------


# students=("anandhakrishnan","ashlin","jeslin","jino")
# students_list=list(students)
# print(students_list)

# students_tuple=tuple(students_list)
# print(students_tuple)