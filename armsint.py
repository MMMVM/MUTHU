d,e=map(int,input().split())
for num in range(d+1,e):
 sum=0
 temp=num
 while temp>0:
  d=temp%10
  sum+=d**3
  temp//=10 
 if(num==sum):
  print(num)
