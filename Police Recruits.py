num_events = int(input())  
event_list = list(map(int, input().split()))  

available_officers = 0  
unhandled_crimes = 0  

for event in event_list:  
    if event == -1:  
        if available_officers > 0:  
            available_officers -= 1  
        else:  
            unhandled_crimes += 1  
    else:  
        available_officers += event  

print(unhandled_crimes)
