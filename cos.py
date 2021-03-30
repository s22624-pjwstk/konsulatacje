class X:
    def make(self,y):
        print("cokolwiek innego",y)
        self.pole=y
        return self

n=X().make(3)
print(n.pole)

s=f':{n}'
print(s)


s="User:"+str(n)
print(s)

s="User:{}".format(n)
print(s)

s=f"User:{n}"
print(s)

s="Ala ma kota"
podmiot="Ala"
o="ma"
pr="kota"
s1=podmiot+" "+o+" "+pr
print(s==s1)
tmp="{b} {a} {c}"
s1=tmp.format(a=podmiot,b=o,c=pr)
print(s1)
print(tmp)