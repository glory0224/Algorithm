# [1차] 캐시

# LRU(Least Recently Used) 캐시 문제 : 가장 최근에 사용되지 않은 항목을 제거하는 캐시 교체 알고리즘

# 새로운 도시가 접근했을 때 cache를 확인하고 cache에 없는 경우 가장 오래된 도시를 제거한 뒤 새로운 도시 추가 

# 입력 형식
# 캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
# cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
# cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
# 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.

# 출력 형식
# 입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.
# 조건
# 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
# cache hit일 경우 실행시간은 1이다. - 이미 기존 데이터가 캐시에 있는 경우
# cache miss일 경우 실행시간은 5이다. - 기존 데이터가 없는 경우

def solution(cacheSize, cities):

    cache = [] # 저장할 캐시 선언

    Time = 0 # 실행 시간

    for city in cities:
        
        city = city.lower() # 대소문자를 구분하지 않고 공백이 없기 때문에 lower를 사용한다.
        
        # hit 인 경우 : 캐시에 이미 들어있음
        if city in cache:
            cache.remove(city) # 이전에 같은 것 빼고  
            cache.append(city) # 새로운 것을 넣는다.
            Time += 1 # hit 시간 추가
        # miss인 경우
        else:
            cache.append(city)
            if len(cache) > cacheSize: # 캐시 사이즈가 넘어간다면 제한된 사이즈보다 넘어간다면
                # 제일 먼저 들어간 자료부터 삭제
                cache.pop(0)
            Time += 5
    
    return Time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 25