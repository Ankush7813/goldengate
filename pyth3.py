album_name = input('TYPE THE ALBUM NAME: ')
# Artist = input('TYPE THE ARTIST NAME: ')
# year = int(input('TYPE THE YEAR OF ALBUM: '))
# songs = input('TYPE THE SONG NAME: ')
# Album_list = [(album_name.upper(), Artist.upper(), year, [songs.upper()])]
Album_list = [('KUSH', 'SNOOP', 2000, ['KUSH']), ('8 MILES', 'eminem', 2000, ['8 MILES'])]
print(Album_list)
tup = ()
while True:
    print("""CHOOSE OPTIONS:
            1. 1 TO ADD NEW ALBUM DETAILS 
            2. 2 TO CHANGE EXISTING ALBUM DETAILS (ALBUM/ARTIST/YEAR ONLY)
            3. 3 TO ADD/REMOVE/UPDATE SONGS IN DEFINED ALBUM
            4. 4 TO CHECK THE YOUR ALBUM DETAILS
            5. 5 TO REMOVE THE WHOLE ALBUM DETAILS
            6. 0 TO TERMINATE THE ALBUM PROGRAM """)
    again = input()

    # TO TERMINATE THE ALBUM PROGRAM
    if again == '0':
        print('THANK YOU FOR YOUR INPUT :)')
        break

    # TO ADD NEW ALBUM DETAILS
    if again == '1':
        print('ADD NEW ALBUM')
        tup = list(tup)  # MAKE EMPTY TUPLE A LIST
        tup.clear()
        album_name1 = input('TYPE THE ALBUM NAME: ')  # USER INPUT
        tup.append(album_name1.upper())  # ADD THE ALBUM NAME IN TUP LIST
        Artist1 = input('TYPE THE ARTIST NAME: ')  # USER INPUT
        tup.append(Artist1.upper())  # ADD THE ARTIST NAME IN TUP LIST
        year1 = int(input('TYPE THE YEAR OF ALBUM: '))  # USER INPUT
        tup.append(year1)  # ADD YEAR(INT ONLY) IN TUP LIST
        songs1 = input('TYPE THE SONG OR SONGS NAME: ')  # USER INPUT
        tup.append([songs1.upper()])  # ADD THE LIST OF SONGS IN TUP LIST
        # CHANGED THE LIST TUP TO TUPLE TUP TO HAVE DATA INTEGRITY IN LIST OF TUPLES
        tup = tuple(tup)
        Album_list.append(tup)  # ADD THE TUP TUPLE IN THE ALBUM LIST
        print(Album_list)

    # TO CHANGE EXISTING ALBUM DETAILS (ALBUM/ARTIST/YEAR ONLY)
    if again == '2':
        print('CHANGE THE ALBUM DETAILS')
        choice2 = input('WRITE THE ALBUM/ARTIST NAME YOU WANT CHANGE: ')  # USER INPUT
        # TO GET THE INDEX VALUES AND TUPLES IN ALBUM LIST
        for index, album_details in enumerate(Album_list):
            if choice2.upper() in album_details:
                user_choices2 = None
                while user_choices2 != '0':
                    print("""PLEASE CHOOSE VALUE TO CHANGE:'
                        1.ALBUM
                        2.ARTIST
                        3.YEAR
                        4. O TO QUIT CHANGES AND SEE MAIN CHOICES
                      """)
                    user_choices2 = input()  # USER INPUT
                    # FOR DEBUGGING ONLY TO CHECK THE INDEX POSITION
                    # print(index)
                    # CHANGE TUPLE ALBUM TO LIST ALBUM - DATA TYPE CHANGE
                    Album_list[index] = list(Album_list[index])
                    # FOR DEBUGGING ONLY
                    # print(Album_list[index])

                    # TO CHANGE ALBUM NAME
                    if user_choices2 == '1':
                        album_name2 = input('TYPE THE ALBUM NAME: ')  # USER INPUT
                        Album_list[index][0] = album_name2.upper()

                    # TO CHANGE ARTIST NAME
                    elif user_choices2 == '2':
                        Artist2 = input('TYPE THE ARTIST NAME: ')  # USER INPUT
                        Album_list[index][1] = Artist2.upper()

                    # TO CHANGE YEAR VALUE
                    elif user_choices2 == '3':
                        year2 = int(input('TYPE THE YEAR OF ALBUM: '))  # USER INPUT
                        Album_list[index][2] = year2

                    # to come out of while loop
                    elif user_choices2 == '0':
                        print('PLEASE SELECT FROM BELOW CHOICES AGAIN')
                        break

                    # CHANGED THE LIST TO TUPLE TO HAVE DATA INTEGRITY IN LIST OF TUPLES
                    Album_list[index] = tuple(Album_list[index])
                    print('CHANGED ALBUM DETAILS ARE : {}'.format(Album_list[index]))
                    print()  # for space in output
                    print("""TO CHANGE AGAIN CHOOSE OPTIONS FROM BELOW OR **PRESS 0 IF NOTHING TO DO**""")
                break  # to come out of if condition and avoid going to condition else
        else:
            print('{} IS NOT EXIST IN ALBUM LIST'.format(choice2.upper()))
            print('PLEASE SELECT FROM BELOW CHOICES AGAIN:')
            break


    # TO ADD/REMOVE/UPDATE SONGS IN DEFINED ALBUM
    if again == '3':
        print('*************ADD/UPDATE/REMOVE THE SONG IN ALBUM*************')
        choice3 = input("WRITE THE ALBUM/ARTIST'S NAME: ") # USER INPUT
        # TO GET THE INDEX VALUES AND TUPLES IN ALBUM LIST
        for index, album_details in enumerate(Album_list):
            # CHECK IF THE USER INPUT EXISTS IN ALBUM DETAILS
            if choice3.upper() in album_details:
                print("'{}' ALBUM/ARTIST'S ALBUM HAVE THESE DETAILS '{}'".format(choice3.upper(), album_details))
                user_choices3 = None
                while user_choices3 != '0':
                    print("""CHOOSE:'
                            1.ADD SONG NAME
                            2.UPDATE SONG NAME
                            3.REMOVE SONG NAME
                            4.O TO QUIT CHANGES AND SEE MAIN CHOICES""")
                    user_choices3 = input() # USER CHOICES

                    # TO ADD THE SONG IN THE SONG LIST OF ALBUM(TUPLE)
                    if user_choices3 == '1':
                        print('*************ADDING SONG*************')
                        # USER INPUT TO ADD THE SONG
                        add_song = input('PLEASE WRITE THE SONG YOU WANT TO ADD: ')
                        # CONDITION TO CHECK IF USER INPUT EXIST IN ALBUM OR NOT
                        if add_song.upper() not in album_details[3]:
                            # IF ABOVE CONDITION TRUE THEN ADD THAT SONG IN SONG LIST(INDEXING OF TUPLE)
                            album_details[3].append(add_song.upper())
                            # INDEXING TO GET THE SONG ALBUM NAME
                            print("'{}' IS SUCCESSFULLY ADDED IN '{}' ALBUM /ARTIST'S ALBUM".format(add_song.upper(), album_details[0]))
                        else:
                            # IF USER INPUT EXISTS THEN PRINT MESSAGE  # INDEXING TO GET THE SONG ALBUM NAME
                            print("'{}' SONG ALREADY EXISTS IN THE '{}' ALBUM /ARTIST'S ALBUM".format(add_song.upper(), album_details[0]))
                        print(album_details)
                        print('*****************#####*****************')
                    # TO UPDATE THE SONG IN SONG LIST IN ALBUM(TUPLE)
                    elif user_choices3 == '2':
                        print('*************Update SONG*************')
                        print("LIST OF SONGS IN ALBUM/ARTIST'S ALBUM:'{}' ".format(choice3.upper()))
                        # LIST OF SONGS
                        print(album_details[3])
                        # USER INPUT
                        replaced_song = input('PLEASE WRITE THE SONG YOU WANT TO REPLACE: ')
                        # CHECK IF USER INPUT IN SONGS LIST (INDEXING OF TUPLE)
                        if replaced_song.upper() in album_details[3]:
                            # TO GET THE INDEX VALUES AND RESPECTIVE SONG IN ALBUM LIST(LIST UNPACKING)
                            for song_index, song in enumerate(album_details[3]):
                                # FOR DEBUGGING ONLY
                                # print(song_index, song)
                                # USER INPUT
                                update_song = input('PLEASE PUT THE SONG NAME FOR REPLACED SONG: ')
                                # ITEM ASSIGNMENT IN LIST
                                album_details[3][song_index] = update_song.upper()
                                # INDEXING TO GET THE SONG ALBUM NAME IN BELOW PRINT
                                print("""'{}' IS REPLACED/UPDATED BY '{}' IN '{}' ALBUM/ARTIST'S ALBUM""".
                                      format(replaced_song.upper(),update_song.upper(),album_details[0]))
                                break
                        else:
                            # IF USER INPUT NOT EXISTS THEN PRINT MESSAGE #  # INDEXING TO GET THE SONG ALBUM NAME
                            print("'{}' SONG NOT EXISTS IN '{}' ALBUM/ARTIST'S ALBUM,PLEASE ADD IT OR CHECK SONG AGAIN".format(
                                replaced_song.upper(), album_details[0]))
                        print(album_details)
                        print('*****************#####*****************')
                    # TO REMOVE THE SONG IN SONG LIST IN ALBUM(TUPLE)
                    elif user_choices3 == '3':
                        print('*************REMOVING SONG*************')
                        print("LIST OF SONGS IN '{}' ALBUM/ARTIST'S ALBUM".format(choice3.upper()))
                        # LIST OF SONGS FOR USER READABILITY
                        print(album_details[3])
                        # input from user
                        remove_song = input('please write the song you want to Remove: ')
                        # CONDITION TO CHECK IF SONG EXITS IN SONG LIST (INDEXING ON ALBUM)
                        if remove_song.upper() in album_details[3]:
                            # USED REMOVED METHOD OS LIST TO REMOVE THE SONG FROM LIST
                            album_details[3].remove(remove_song.upper())
                            # INDEXING TO GET THE SONG ALBUM NAME IN BELOW PRINT
                            print("'{}' SONG SUCCESSFULLY REMOVED FROM '{}' ALBUM/ARTIST'S ALBUM".format(remove_song.upper(),album_details[0]))
                        else:
                            # INDEXING TO GET THE SONG ALBUM NAME IN BELOW PRINT
                            print("""'{}' SONG NOT EXISTS IN '{}' ALBUM/ARTIST'S ALBUM, PLEASE ADD IT OR CHECK SONG AGAIN WHICH YOU WANT TO REMOVE'""".
                                  format(remove_song.upper(), album_details[0]))
                        print(album_details)
                        print('*****************#####*****************')
                    # to come out of while loop
                    elif user_choices3 == '0':
                        break
                print('*****************#####*****************')
                break # to come out of if condition and avoid going to condition else
        else:
            print("'{}' ALBUM/ARTIST'S ALBUM IS NOT EXIST IN ALBUM LIST".format(choice3.upper()))
            break
    # # 4 TO CHECK THE YOUR ALBUM DETAILS
    # if again == '4':
    #     print('ALBUM DETAILS')
    #     # USER INPUT
    #     choice4 = input('PLEASE WRITE THE ALBUM/ARTIST/SONG OR YEAR YOU WANT TO CHECK: ')
    #     # TO GET THE INDEX VALUES AND TUPLES IN ALBUM LIST
    #     for index, album_details4 in enumerate(Album_list):
    #         # CHECK IF USER INPUT EXISTS IN ALBUM TUPLES
    #         if choice4.upper() in album_details4:
    #             print("""{} ALBUM DETAILS Is below: {}""".format(choice4, album_details4))
    #
    #
    #
    #     elif choice4.upper() not in album_details4:
    #         print('{} ALBUM DONT EXIST IN ALBUM_LIST'.format(choice4.upper()))
    # # TO REMOVE THE WHOLE ALBUM DETAILS
    # if again == '5':
    #     print('REMOVE WHOLE ALBUM DETAILS FROM ALBUM LIST')
    #     # USER INPUT
    #     choice5 = input('PLEASE WROTE THE ALBUM/ARTIST/SONG OR YEAR YOU WANT TO REMOVE: ')
    #     for index, album_details5 in enumerate(Album_list):
    #         if choice5.upper() in album_details5:
    #             # removing the whole tuple from list
    #             cache_add= Album_list.pop(index)
    #             print(index)
    #             print(cache_add)
    #             confirmation_check=input('ARE YOU SURE YOU WANT TO REMOVE IT, IF YES THEN TYPE - Y , IF NOT THEN N : ')
    #             if confirmation_check.upper() == 'N':
    #                 Album_list.insert(index,cache_add)
    #             else:
    #                 print('YOUR CHOICE {} IS SUCCESSFULLY REMOVING {} FROM ALBUM LIST'.format(choice5.upper(),cache_add))
    #                 print(Album_list)
    #             break
    #         else:
    #             print('{}  IS NOT IN ALBUM LIST PLEASE CHECK AGAIN'.format(choice5))
    #             break



