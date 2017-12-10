#Exercise 4

#Aufgabe 4_3

#Zeichen festlegen
linewidth = 20
empty = '.'
full = '#'

#Funktionen definieren
def emptyline():
    print(empty*lindewidth)

def fromto(begin, end):
    s = ' '
    for i in range(0, begin):
        s = s + empty
    for i in range(begin, end):
        s = s + full
    for i in range(end, linewidth):
        s = s + empty
        
print('You love ASCII art? Yes/No')
x = input()
if x == 'Yes':
    print("""\

                         #....................#
                         .#..................#.
                         ..#................#..
                         ...#..............#...
                         ....#............#....
                         .....#..........#.....
                         ......#........#......
                         .......#......#.......
                         ........#....#........
                         .........#..#.........
                         ..........##..........
                         .........#..#.........
                         ........#....#........
                         .......#......#.......
                         ......#........#......
                         .....#..........#.....
                         ....#............#....
                         ...#..............#...
                         ..#................#..
                         .#..................#.
                         #....................#
/


                    """)
if x == 'No':
    print('Me neither!')
