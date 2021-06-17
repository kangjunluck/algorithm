def solution(record):
    answer = []
    
    datainfo = []
    id_name = {}
    for step in record:
        info = step.split()
        if info[0] == 'Enter':
            id_name[info[1]] = info[2]
            datainfo.append((info[1], 0))
        elif info[0] == 'Leave':
            datainfo.append((info[1], 1))
        else:
            id_name[info[1]] = info[2]
    for id, state in datainfo:
        if state == 0:
            answer.append('{}님이 들어왔습니다.'.format(id_name[id]))
        else:
            answer.append('{}님이 나갔습니다.'.format(id_name[id]))
            
            
    return answer