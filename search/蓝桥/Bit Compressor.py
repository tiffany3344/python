'''
11111111001001111111111111110011
11111111->1000
111111111111111(15)->1111
1000 00100 1111 0011
10 不能解密成11
100 由于0是分割符 100

10000010011110011
'''
#原串长L，原串中1的个数N
L,N = map(int,input().split())
s=input()
E=[]
temp=0
left = N #剩下1的个数
sign = 0 #列表小序列标号
for i in range(len(s)):
    if s[i]=='0' and s[i+1]=='1':
        #分成每个单独的解密部分
        l = s[temp:i+1:]

        temp=i  #上一次截取借宿的地方