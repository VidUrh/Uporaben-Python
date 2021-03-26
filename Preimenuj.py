import os

path = "C:/Users/vidur/Music/So najlepše pesmi že napisane"

pesmi = os.listdir(path)
separator = ' '


for pesem in pesmi:
    try:
        x = pesem[2:].strip()
        ''' x = list(x)
        for a in range(len(x)):
            if x[a] == '_':
                x[a] = ' '
                
        x = x[0].upper() + ''.join(x[1:])'''
        if x.endswith('.flac'):
            x=x.strip('.flac')
            x+='.mp3'
        novnaslov = path+"/"+x
        print(novnaslov)

        #os.rename(path + "/" + pesem, novnaslov)
    except:
        print('Error:',pesem)
        #os.remove(path + "/" + pesem)
   
        #os.rename = path
    '''if not pesem.endswith(".mp3"):
            print(pesem)
        #   os.remove(path + '/' + pesem)

        novnaslov = path + "/" + pesem[18::]
        print(novnaslov)
        '''


'''try:
        pesem2 = pesem.split("-")
        pesem2.pop(0)
        pesem2 = separator.join(pesem2)
        novnaslov = path + "/" + pesem2[1::]                     
        print(novnaslov)
        os.rename(path + "/" + pesem, novnaslov)
    except(WindowsError):
        pass '''
