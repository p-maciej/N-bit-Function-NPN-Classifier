import itertools
from booleanFunction import BooleanFunction
import copy

def combinations(target, data, output):
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_target.append(data[i])
        new_data = data[i+1:]
        output.append(new_target)
        combinations(new_target, new_data, output)

def generateCombinations(bits):
    return list(itertools.product((0,1), repeat=bits))

def generateIrreversibleFunctions(bits):
    inputs = generateCombinations(bits)
    outputs = generateCombinations(len(inputs))

    return inputs, outputs

def makeInputPermutationList(input):
    return list(itertools.permutations(input))

def negateFunction(function):
    output = ()
    for i in range(len(function)):
        output += tuple([int(not function[i])])

    return output


def createFunctionDatabase(inputs, functions):
    database = set()

    for function in functions:
        func = createFunction(inputs, function)
        database.add(func)

    return database

def createFunction(inputs, output):
    func = BooleanFunction()

    for i in range(len(inputs)):
        func.addValue(inputs[i], output[i])

    return func

def makeCombinations(item):
    return itertools.combinations(item, r=len(item))

def generateBooleanFunctionNPNClasses(inputs, functions): #classify NPN functions
    dataset = set()

    inputT = list(zip(*inputs)) # transposed inputs - rows -> columns
    classId = 1
    for function in functions:
        functionNegation = negateFunction(function)
        lenIn = len(dataset)

        #add current function
        func = createFunction(inputs, function)
        func.setClass(classId)

        if func not in dataset:
            dataset.add(func)

            functionsToLookup = []
            #make permutations of inputs
            perm_inp = makeInputPermutationList(inputT)
            for input in perm_inp:
                inputUT = list(zip(*input))

                target = []
                toNegate = []

                combinations(target, range(len(input)), toNegate)

                # create input negations
                input_negations = []

                for negateArray in toNegate:
                    neg = []
                    for index in range(len(input)):
                        if index in negateArray:
                            neg.append(negateFunction(input[index]))
                        else:
                            neg.append(input[index])
                    input_negations.append(neg)

                inputNegationtUT = []
                for inputNeg in input_negations:
                    inputNegationtUT.append(list(zip(*inputNeg)))

                functionsToLookup.append(createFunction(inputUT, function))         #without output negation
                functionsToLookup.append(createFunction(inputUT, functionNegation)) #with output negation
                for inp in inputNegationtUT:                                        #combinations of negation of inputs
                    functionsToLookup.append(createFunction(inp, function))
                    functionsToLookup.append(createFunction(inp, functionNegation))

            for func in functionsToLookup:
                func.setClass(classId)
                dataset.add(func)


            lenOut = len(dataset)
            if(lenOut - lenIn > 0):
                classId += 1

        if len(dataset) == len(functions):
            break

    return dataset

inputs, functions = generateIrreversibleFunctions(4) # generated functions
dataset = generateBooleanFunctionNPNClasses(inputs, functions)
dataset = sorted(dataset) # sorted by functions

for item in dataset:
    print(item)


