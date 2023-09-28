def compress_string(string):
    if not string:
        return ''

    compress = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else: 
            compress.append(string[i-1] + str(count))
            count = 1
    
    compress.append(string[-1] + str(count))
    compress_string = ''.join(compress)

    if len(compress_string) < len(string):
        return compress_string
    else:
        return string
    
og_string = "aabcccccaaa"
compressed = compress_string(og_string)
print(compressed)
#Implement a method to perform basic string compression using the counts
#of repeated characters. For example, the string a a b c c c c c a a a would become a 2 b l c 5 a 3 , If the
#"compressed" string would not become smaller than the original string, your method should return
#the original string. You can assume the string has only uppercase and lowercase letters (a - z



