num_samples,sample_len=list(map(int,input().split()))

unlikeliness=0
s=input()
for _ in range(num_samples-1):
    sample=input()
    al_ready=set()
    for j in range(sample_len):
        if s[j]!=sample[j] and (sample[j] not in al_ready):
            unlikeliness+=1
            al_ready.add(sample[j])
    s=sample

print(unlikeliness)