import sys
def main():
    a,b,c,v0,v1,v2=map(int,input().split())
    opt1=a/v0+a/v1+b/v0+b/v1
    opt2=b/v0+b/v1+a/v0+a/v1
    opt3=a/v0+c/v1+b/v2
    opt4=b/v0+c/v1+a/v2
    opt5=a/v0+a/v1+b/v0+c/v1+a/v2
    opt6=b/v0+b/v1+a/v0+c/v1+b/v2
    opt7=a/v0+a/v1+c/v0+b/v1
    opt8=b/v0+b/v1+c/v0+a/v1
    ans=min(opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8)
    print(ans)
if __name__=='__main__':
    main()