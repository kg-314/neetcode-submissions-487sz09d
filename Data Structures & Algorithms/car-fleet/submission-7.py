class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Calculate arrival times for each car (1st).

        # Sort cars so highest to lowest by starting position (2nd)

        # Cars with earlier arrival time but lower starting position 
        # become a single fleet with the first car (3rd)

        # Use stack to keep popping cars with earlier arrival time than first car
        # in fleet

        # Arr time = (10 - position) / speed

        # floats allowed

        cars = [] # my stack

        for i in range(len(position)):
            p = position[i]
            s = speed[i]

            arrTime = float((target - p) / s)
            cars.append([float(p), arrTime])

        cars.sort(key=lambda x: x[0])

        output = 1

        first = cars.pop()

        while cars:
            nextCar = cars.pop()

            if nextCar[1] > first[1]:
                output += 1
                first = nextCar
        return output

