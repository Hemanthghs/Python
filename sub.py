import random
lang_list=['c','cpp','py','swift','jl','java','js','go','rb','NET','txt','lsp']

for i in range(1,1001):
    print("submission"+str(i)+"."+lang_list[random.randint(0,11)]+"\n")
