for i in range(1, 175000):
    if ''.join(sorted(str(i*2))) == ''.join(sorted(str(i))):
        if ''.join(sorted(str(i*3))) == ''.join(sorted(str(i))):
            if ''.join(sorted(str(i*4))) == ''.join(sorted(str(i))):
                if ''.join(sorted(str(i*5))) == ''.join(sorted(str(i))):
                    if ''.join(sorted(str(i*6))) == ''.join(sorted(str(i))):
                        print(i)
                        break
