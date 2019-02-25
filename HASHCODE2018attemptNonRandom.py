#condensed version of non-random ride allocations
import random
import pdb
import sys



try:
    f =  int(sys.argv[1])
    if f==1:
        filenameToUse = file1 = "data_files\\a_example.in"
    elif f==2:
        filenameToUse = "data_files\\b_should_be_easy.in"
    elif f==3:
        filenameToUse = "data_files\\c_no_hurry.in"
    elif f ==4:
        filenameToUse = "data_files\\d_metropolis.in"
    else:
        filenameToUse = "data_files\\e_high_bonus.in"

except IndexError:
    print("No filename selection given (1-5)")
    filenameToUse =  "data_files\\a_example.in"  # no ar given

try:
    versionToUse = int(sys.argv[2])
except IndexError:
    print("No version given (1-2)")
    versionToUse = 1  # no

inputfile = open(filenameToUse,"r")
header = inputfile.readline().rstrip('\n').split(" ")

rides = []
for line in inputfile:
    rides.append([int(x) for x in line.rstrip('\n').split(" ")])
inputfile.close()

rows = int(header[0])
columns = int(header[1])
vehicle_count = int(header[2])
ride_count = int(header[3])
bonus_value = int(header[4])
timesteps = int(header[5])

#***WEIGHTINGS***
# include some weightings to help rank the best ride to pick
distanceToStartWeight = -5
bonusWeight = 1
waitWeight = -5
rideDistanceWeight = 0
distanceFromCentroidWeight = 1


print(rows, " rows, ", columns," columns, ", vehicle_count, " vehicle_count, ", ride_count," ride_count, ", bonus_value," bonus_value, ", timesteps," timesteps")

#work out the centroid of all ride starting points
#plus append distance to each ride

centroidX = 0.0
centroidY = 0.0

for r in rides:
    r.append(abs(r[2]-r[0])+abs(r[3]-r[1]))
    centroidX += r[0]
    centroidY += r[1]
    r.append(0)

centroidX = centroidX/ride_count
centroidY = centroidY/ride_count



print("centroid ", centroidX,", ",centroidY)


#create a list of vehicles, each v is an array [currentRide,currentRideEndTimeStep,currentX,currentY]
#if currentRide = -1 the vehicle does not have a ride and can look for one

def canVehicleDoRide(t,vX, vY, rStartX, rStartY, rDist, rEarliestStart, rLatestFinish,rDistanceFromCentroid ):
    #print("canVehicleDoRide(",t,",",vX,",", vY,",", rStartX,",", rStartY,",", rDist,",", rEarliestStart,",", rLatestFinish,")")
    distanceToStart = (abs(rStartX-vX)+abs(rStartY-vY))
    waitTime =  (rEarliestStart - (t + distanceToStart))

    if waitTime < 0: #if wait time is negative you do not wait at all, so set to 0
        waitTime = 0

    eta = (t + distanceToStart + waitTime + rDist)
    if eta > rLatestFinish:
        return [-1,-1]
    else:
        #this ride can be done- work out a score using weightings
        rankbonus = 0
        if (t + distanceToStart <= rEarliestStart):
            rankbonus=bonus_value

        rankscore = (distanceToStart*distanceToStartWeight) + (rankbonus*bonusWeight) + (waitTime*waitWeight) + (rDist*rideDistanceWeight) + (rDistanceFromCentroid*distanceFromCentroidWeight)
        return [eta,rankscore]



#set up assignments
assigned_rides = [[] for x in range(vehicle_count)]

if versionToUse == 1:
    #begin version 1

    #print(assigned_rides)
    for i, r in enumerate(rides):
        #print(i)
        random_v = random.randint(0,vehicle_count-1)
        #print(random_v)
        assigned_rides[random_v].append(i)
    print("assigned all rides randomly")
    #end version 1
elif versionToUse == 2:
    #begin version 2
    vehicles = [[-1,-1,0,0,1] for x in range(vehicle_count)]


    ##add an element to rides to track their completion

    #canDo = [[[1] for y in range(rides)] for x in range(vehicle_count)]
    canDo = [[1 for i in range(ride_count)] for j in range(vehicle_count)]
    #print(canDo[0][0])

    shuffleSequence = [x for x in range(ride_count)]


    for r in rides:
        if len(r) < 8:
            r.append(0);
        else:
            r[7] = 0;
        if len(r) < 9: #also need to check if a ride is eliminated because it cannot be done
            r.append(0);
        else:
            r[8] = 0;
        if len(r) < 10: #precaluculate the distance of the end of the ride to the centroid of all rides
            r.append( int(abs(r[2]-centroidX)+abs(r[3]-centroidY)));
        else:
            r[9] = 0;


    #print(rides)
    t = 0
    while t < timesteps:
        minNextUsedTimeStep = -1 #can skip timesteps where no rides end

        if t % 1000 == 0:
            print("Timestep = " + str(t)); #just so there is some output every so often


        #first check if there are any more rides to assign at all -
        #first remove any rides that can no longer be done
        for rc in rides:
            if r[5] < t:
                rc[8] = 1 #this ride can no longer be done as finish time has expired

        unassignedRideExists = False
        for rc in rides:
            if rc[8] == 0 and rc[7] == 0:
                unassignedRideExists =  True;
                break;

        usableVehicleExists = False
        for v in vehicles:
            if v[4] == 1:
                usableVehicleExists = True
                break


        if unassignedRideExists == False:
            print("All rides assigned or undoable, timestep " + str(t));
            break;
        elif usableVehicleExists == False:
            print("All vehicles unusable, timestep " + str(t));
            print("vehicles " + str(vehicles));
            break;

        #for each timestep (with rides left to assign) look at each vehicle

        #idea 6: randomize the path through the rides
        #random.shuffle(shuffleSequence)
        #print("shuffleSequence = ", shuffleSequence)

        for  i, v,  in enumerate(vehicles):
            # is this vehicle usable?

            if v[4] == 1:
                #check to see if a ride finishes this timestep
                if v[1] == t:
                    #print("Ride " + str(v[0]) + " on vehicle " + str(i) + " finishes now (timestep " + str(t) + ")")
                    v[0] = -1 #finishes, so can look for another ride
                    v[1] = -1 #reset the finishing timestep

                if v[0] == -1:
                    #print("vehicle " + str(i) + " can look for a ride")
                    #loop through rides to find an available one

                    selectedRideMaxScore=-1000000
                    selectedRideIndex=-1
                    selectedRideFinishTime=0

                    for k in shuffleSequence:#should go through rides- can be randomised

                        r = rides[k]
                        #print(r,canDo[i][k])
                        if r[8] == 0 and r[7] == 0 and canDo[i][k] == 1:
                            #this ride has not been assigned so could be assigned
                            #can this car actually do this ride?
                            canDoNow = canVehicleDoRide(t, v[2], v[3], r[0], r[1], r[6], r[4], r[5],r[9] )
                            #print("canDoNow = " + str(canDoNow),k,t, v[2], v[3], r[0], r[1], r[6], r[4], r[5] )
                            if canDoNow[0] > 0:
                                #print("Vehicle ",i," can do ride ",k," ", r, " with rank ", canDoNow)
                                #canDo[i][k] = canDoNow[0]
                                if canDoNow[1] > selectedRideMaxScore:
                                    selectedRideMaxScore = canDoNow[1]
                                    selectedRideIndex = k
                                    selectedRideFinishTime = canDoNow[0]
                            else:
                                #this vehicle will never be able o do this ride so don't check again
                                canDo[i][k] = 0
                    #assign a ride if options were found


                    if(selectedRideIndex >= 0):
                        rides[selectedRideIndex][7] = 1
                        v[0] = selectedRideIndex
                        v[1] = selectedRideFinishTime
                        assigned_rides[i].append(selectedRideIndex)
                        canDo[i][selectedRideIndex] = 0 #vehicle can only do a ride once- might not be needed as ride will be marked as done
                        #print("Assigned ride " + str(selectedRideIndex) + " to vehicle "+ str(i) )
                        #move the vehicle location to the end of the assigned ride
                        v[2] = r[2]
                        v[3] = r[3]
                        #if no ride assigned this vehicle is unusable from now on
                    if v[0] == -1:
                        #print("Vehicle ", v, " is no longer usable, timestep ", t)
                        v[4] = 0

                if v[0]>0: # check if this vehicle is the next to finish
                    if minNextUsedTimeStep == -1:
                        minNextUsedTimeStep = v[1]
                    elif v[1] < minNextUsedTimeStep:
                        minNextUsedTimeStep = v[1]


        if minNextUsedTimeStep > 0:
            #print("Jumping to timestep: " + str(minNextUsedTimeStep))
            t=minNextUsedTimeStep #can skip timesteps until the next change
        else:
            t+=1 #go to next timestep

    #count the rides that were assigned- were some not done?
    totalAssigned = 0
    for r in rides:
        totalAssigned+= r[7]

    print(str(totalAssigned) + "/" + str(len(rides)) + " Rides Assigned" )
    #end version 2

else:
    print("Invalid version, 1 = random, 2 = non random")

#save to output file
outputfile = open("HASHCODE2018attemptv1.txt","w")
for key, value in enumerate(assigned_rides):
    s = "" + str(key)
    #print(value)
    for v in value:
        s+= " " + str(v)
    #print(s)
    outputfile.write(s+"\n")
outputfile.close()


#work out the score
print("Work out the score")
score = 0
canFinishCounter = 0
totalRidesAllocated = 0
bonusPoints = 0
for key, value in enumerate(assigned_rides):
    location = [0,0] #all vehicles start at 0, each ride will leave them at a different point
    timeCounter = 0
    vehicleScore = 0

    for v in value:
        totalRidesAllocated+=1
        rideScore = 0
        ride = rides[v]
        startX = ride[0]
        startY = ride[1]
        endX = ride[2]
        endY = ride[3]
        earliestStart = ride[4]
        latestFinish=ride[5]
        distance = ride[6]

        distanceToStart = (abs(startX-location[0])+abs(startY-location[1]))
        waitTime =  (earliestStart - (timeCounter + distanceToStart))
        if waitTime < 0: #if wait time is negative you do not wait at all, so set to 0
            waitTime = 0

        #can you actually do the ride at all?
        EstimatedTimeFinished = (timeCounter + distanceToStart + waitTime + distance)
        canFinish = (EstimatedTimeFinished <= latestFinish) # True or False

        #if you can finish it, add the score and move the location and time on
        bonus = 0


        if canFinish:
            canFinishCounter+=1
            #do they get a bonus?
            if (timeCounter + distanceToStart <= earliestStart):
                bonus=bonus_value
                bonusPoints += bonus
            #print("Vehicle ",key , ", Ride ",key, " from (",ride[0],",",ride[1],") to (",ride[2]," to ", ride[3],"),")
            #print("distanceToStart:",distanceToStart, "earliestStart:",earliestStart,"waitTime:",waitTime,", distance:",distance)
            #print("EstimatedTimeFinished: ",EstimatedTimeFinished,", latestFinish:",latestFinish,", canFinish:",canFinish,", bonus:",bonus)
            rideScore += distance + bonus
            score+=rideScore
            #print("rideScore = " , rideScore)
            vehicleScore += rideScore
            location = [endX,endY]
            timeCounter += distanceToStart + waitTime + distance
            #print("Adjusted location: (",endX, ",",endY,"), timeCounter:",timeCounter)

    #print("Vehicle Score = ", vehicleScore)

print("Filename used '" + filenameToUse + "', algorithm version " + str(versionToUse))
print("Total Bonus = " + str(bonusPoints))
print("Can Finish " + str(canFinishCounter) + "/ " + str(totalRidesAllocated))
print("TOTAL SCORE = " + str(score))
