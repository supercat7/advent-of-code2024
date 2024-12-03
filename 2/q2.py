from os.path import dirname
lines = []
with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()
safe_report_num = 0

for i in lines:
    arr = list(map(int, i.split()))
    distance_true = None
    bad_count = 0
    for i in range(0, len(arr)-1):
        dist = arr[i] - arr[i+1]
        if abs(dist) < 4 and dist != 0:
            if distance_true in (True, None) and bad_count == 0:
                distance_true = True
        elif abs(dist) >= 4 or dist == 0:
            distance_true = False
            bad_count += 1
    


    if distance_true == True:
        if (all(i < j for i, j in zip(arr, arr[1:]))) or (all(i > j for i, j in zip(arr, arr[1:]))):
            safe_report_num += 1
        else:
            bad_count += 1
            distance_true = False   
    elif distance_true == False and bad_count == 1:
        safe_report_num += 1
print(safe_report_num)
