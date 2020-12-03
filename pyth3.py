Albums=[
    ('kush','snoop dog',2000,['kush','ganja','doggie style']),
    ('8 miles','eminem',2008,['8 miles','never stop','one game']),
    ('kamikaze','eminem',2018,['kamikaze','the river','aint gona play']),
    ('dre 2001','dr dre',2001,['still dre','san andrias','welcome candy shop'])
    ]
while True: # this will the below print again and again until a break is not used at same indent level .. check line 15
    print('Please choose your album')
    for index,(Album, artist, year, songs) in enumerate(Albums): # unpacking
        print('{}: {}'.format(index+1,Album)) 
    choice=int(input())
    if 1<= choice <=(len(Albums)):
        songs_list=Albums[choice-1][3] # to get the song list by indexing and puting it in diff variable
    else:
        print('Ops! wrong choice Terminated')
        break  # break to terminate the program if invalid choice
    while True:
        print('please choose song')
        for index , songs in enumerate(songs_list): # unpacking
            print('{}: {}'. format(index+1,songs))
        song_choice=int(input())
        if 1 <= song_choice <= (len(songs_list)):
            Play_song=songs_list[song_choice-1] # to get desired song from song list according to user choice
            print('Playing song {} from {}'.format(Play_song,Albums[choice-1][0])) 
            break  # break from inner while if correct answer
        else:
            print('Your chioice is wrong please choose again')
            break  # break from inner while # we can comment Break to print the song list again if want user to choose song again else no break will be fine
        
    


