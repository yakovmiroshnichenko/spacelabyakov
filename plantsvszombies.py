def plants_vs_zombies(zombies, plants, counter = None):
    counter = len(plants) - len(zombies)
    for i in range(min(len(plants), len(zombies))):

        if int(plants[i]) - int(zombies[i]) > 0:
            counter += 1
        if int(plants[i]) - int(zombies[i]) < 0:
            counter -= 1

    if counter > 0:
        return True
    if counter < 0:
        return False
    else:
        if counter == 0:
            if sum(plants) >= sum(zombies):
                return True
            else:
                return False

print(plants_vs_zombies([1,3,5,7],[2,4,6,8]))
print(plants_vs_zombies([1,3,5,7],[2,4]))
print(plants_vs_zombies([1,3,5,7],[2,4,0,8]))
print(plants_vs_zombies([2,1,1,1],[1,2,1,1]))