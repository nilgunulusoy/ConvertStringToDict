
string="QUERY_STRING='adi=can&soyadi=aydın&yas=35&il=izmir'"
a=string[string.find("\'")+1: string.find("\"")]

d={}
for i in a.split('&'):
    for m in i.split('='):
        d.update({i.split('=',1)[0]:i.split('=',1)[1]})
                 
             
    
print(d)
