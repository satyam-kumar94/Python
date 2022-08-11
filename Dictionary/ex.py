from turtle import update


myDict = {
    "satyam": "i am quick learner",
    "work": "i am coder",
    "marks": [2,3,4,5],
    "anotherdict":{'satyam': 'coder'},
    1: 2
}
# print(myDict['satyam'])
# print(myDict['work'])
# print(myDict['marks'])
# print(myDict['anotherdict']['satyam'])


# dictionary method
print(myDict.keys())
print(list(myDict.keys()))
print(myDict.values())
print(myDict)
updateDict ={ #update dictionary
    "anmol":"saurabh",
    "work": "study"
}
myDict.update(updateDict)
print(myDict)
print(myDict.get("satyam")) #get value from dictonary




