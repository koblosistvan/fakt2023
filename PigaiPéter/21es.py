def huszonegyes(lapsor, játékossor):
    a = 0
    b = 0
    for i in range(len(játékossor)):
        if játékossor[i] == 'A':
            a += lapsor[i]
        elif játékossor[i] == 'b':
            b += lapsor[i]
    if 21 >= a > b:
        print(f'"A"({a}) játékos nyert')
    elif 21 >= b > a:
        print(f'"B"({b}) játékos nyert')
    elif a > 21 >= b:
        print(f'"A"({a}) játékos befuccsolt, "B"{b} játékos nyert')
    elif b > 21 >= a:
        print(f'"B"({b}) játékos befuccsolt, "A"({a}) játékos nyert')
    else:
        print(f'Mindkét játékos befuccsolt {a},{b}')
