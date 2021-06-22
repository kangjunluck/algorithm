def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    n = len(str1)
    m = len(str2)
    str1_list = {}
    str2_list = {}
    for i in range(n-1):
        if str1[i:i+2].isalpha():
            str1_list[str1[i:i+2]] = str1_list.get(str1[i:i+2], 0) + 1
    for j in range(m-1):
         if str2[j:j+2].isalpha():
            str2_list[str2[j:j+2]] = str2_list.get(str2[j:j+2], 0) + 1
    hap = {}
    cha = {}
    
    for keya in str1_list:
        hap[keya] = str1_list[keya]
    
    for keyb in str2_list:
        if keyb in hap.keys() and hap[keyb] >= str2_list[keyb]:
            continue
        hap[keyb] = str2_list[keyb]
    hap_cnt = sum(hap.values())
    
    strr = str2_list
    st = str1_list
    if len(str1_list) > len(str2_list):
        strr = str1_list
        st = str2_list
    cha = 0
    for key in strr:
        if key in st.keys():
            cha += min(st[key], strr[key])

    if hap_cnt == 0:
        answer = 65536
    else:
        answer = int(cha/hap_cnt*65536)

    
    return answer