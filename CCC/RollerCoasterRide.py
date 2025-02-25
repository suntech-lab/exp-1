iPlaceInLine = int(input())
iTrainCars = int(input())
iCarCapacity = int(input())

if iPlaceInLine <= iTrainCars*iCarCapacity:
    print("yes")
else:
    print("no")