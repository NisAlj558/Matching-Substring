string =input('Entetr string :')
start =input('Entetr start litter :')
end =input('Entetr end litter :')
def countSubstring(string,start,end) :
    totalCount= 0
    count= 0
    for i in string :
        if i==start :
            count=count+1
        if i==end :
            totalCount=totalCount+count
    return print('count:',totalCount)
countSubstring(string,start,end)
