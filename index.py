# askljdasoulbpasdubasbas dashdhashd ashdjhashdapdo;c;a;lkjsafa;al;sdjlkasdjkasd';lsjdf;sadfa'dfs'saf'as;;
# string="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
string=input('Masukkan Kata untuk dihitung huruf penyusunnya: ')
contain=set()
for letter in string:
    if letter.isalpha():
        contain.add(letter.lower())
print("Jadi ada",len(contain),"huruf, yaitu : ")
print(sorted(contain))