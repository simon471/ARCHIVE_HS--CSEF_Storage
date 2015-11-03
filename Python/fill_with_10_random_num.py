def main():
    a=zeros(40)
    for i in range(len(a)):
        a[i]=sum_array(rand_array(10,0,1))
    histo=histogram(0.,10.,7,a)
    bargraph(histo)
main()
