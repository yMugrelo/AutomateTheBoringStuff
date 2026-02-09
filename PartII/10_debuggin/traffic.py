def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow' 
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

market_2nd = {'ns' : 'green', 'ew' : 'red'}

switchLights(market_2nd)

assert market_2nd == {'ns' : 'yellow', 'ew' : 'green'}

print("All tests passed!")