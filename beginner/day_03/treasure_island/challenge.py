print('''
                                   /     / ^^--_
                                  /    ./     ,'^-.
                                 /`.  / ^-_ ,'     `.               ,--.
                                 |   /     ^-_     _-\           ,--^--^-.
                                 \   \        \_-     \         /         \
                                 .>  /    `.-_|        \        | ,--^^^-- \
                            ,.-^^ \,'     / `.`.       ~\       |/        ' \
                            `'--~~'       |   `.`.      `._-^>  |           |
                                          |     `.\     ,'_-^   |           |
                                          \       \\   /,' /    \           |
                                           \O      \`.'/  /      \   ,-^^-_ |
                                            \       / \O_/        \ (__--\ \/
                                             \,'^`.     |          `,^--_ \ \
                                             / i . `-___\         ,^--_. ^^--_.
                                            (+-+-+-+-+-\         '_',-:.^-_ >  \
                                             \ l '_-''^~/'         |   |   >   |
                                              `.,'    ,'           |   |       |
                                              /     ,'             |   |      /
                                             /    ,' __--__         \_/      /
                                      __---^/   ,'_-^      ^-_       |      |
                         ,--,--^^^--,'     /    ,'            `.     \      |
                       ,'  /     ,':^-__----^^^/                \     |    /
                     ,'        ,' ,'`^--^^,','/          _-^^^-_|     |    |
                    /         / ,'      ,','  |        ,'       `.    |    |
                   /   /     / /      ,','            (           \  /      \
                   |  /     / /     ,','               \           \'        i
                   |  |.   / /    ,','                 |          /          |
                   /  \ ^-_| |  ,','                   |         /\          |
                  i    \   | |,','-___               _-^\       i  `.        |
                  |    /   \ ','      ^^^^---____--^^    \      \    ^-_     |
                  |   /    / <                   /        `.     `.     ^^--_l
                  \  /    / /\`.               ,'           `.     ^-_      /
             ,-^^-J  |   / /  \ \           _-^               `.      ^^--_/
._-^~~^.   ,'  `.`.   \ / /    \ \        ,'                    `-_      ,'
|`---'  ^v^      \ \   Y /      \ \     :'                         ^-__.'
|-_____)          \ \ / /        \ \     |
|-_____)          | /| /          \ i    /
\=___)___---^^^^---J '/           | |__-^l
  `^^'             i`-------------^^^   ,'
                   `._________________-'
                   |                  \
                   /                   |
                 ,'                    |
               ,'      ,-__-.         /
             ,'      ,'      `>      |
           ,'      ,'        /       |
          /       /          |       |
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision1 = input('Where do you want to go? Type "left" or "right".\n').lower()


if decision1 == "right":
    decision2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swin" to swin across.\n').lower()
    if decision2 == "wait":
        decision3 = input('Your arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n')
        if decision3 == "red":
            print("It's a room full of fire. Game over")
        elif decision3 == "yellow":
            print("You found the treasure! You win!")
        elif decision3 == "blue":
            print("You enter a room of beasts. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")