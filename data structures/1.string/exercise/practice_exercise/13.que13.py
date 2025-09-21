# 13. Count the number of vowels and consonants in 'programming'.

a="programming"
vowels=['a','e','i','o','u']
vowel_cnt=0
for x in a:
    if x in vowels:
        vowel_cnt+=1
print("no of vowels",vowel_cnt)
print("no of consonants",len(a)-vowel_cnt)