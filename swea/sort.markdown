# 정렬

## 정렬이란
  - 2개 이상의 자료를 특정 조건에 따라 재배열 하는것( 오름차순, 내림차순 )
  - 정렬 알고리즘의 종류가 여러개인 이유 : 정렬 알고리즘 별로 시간 복잡도나 효율성이 다르기 때문.

## 버블 정렬
- 배열의 앞뒤를 비교하며 큰 수를(오름차순 기준) 계속해서 뒤로 보내 정렬하는 알고리즘

### 특징
- 시간 복잡도 : 최악 = O(n^2) , 최선 =  O(n)
- 적응성, 안정성 : O
- 제자리 정렬(새 메모리 쓰지 않음) : O

###  예시
```python
# code
arr = [6,3,2,5,3]

for i in range(1, len(arr)-1):
  flag = False
  for j in range(len(arr)-i):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j]
      flag = True
    if not flag:
      break

print(arr) # [2,3,3,5,6]

```
## 선택 정렬
- 배열의 요소들을 돌며 차례대로 작은값의 원소부터 선택하여 원소를 교환하는 방식

### 특징
- 시간 복잡도 : O(n^2)
- 안정성, 적응성 : X
- 제자리 정렬 : O
### 코드 
```python
# code
arr = [6,2,3,5,6]

for i in range(len(arr)-1):
  min_idx = i
  for j in range(i+1,len(arr)):
    if arr[min_idx] > arr[j]:
      min_idx = j
  arr[i],arr[min_idx] = arr[min_idx], arr[i] 

print(arr) # [2,3,5,6,6]
```
## 삽입 정렬
- 정렬된 자료 S와 정렬되지 않은 원소 U로 나뉘어 U의 값을 S에서 하나씩 비교하며 삽입하는 방식
- 안정성, 적응성 : O
- 제자리 정렬 : O


### 코드
```python
#code 
arr = [5,2,1,4,7]
for i in range(1,len(arr)):
  for j in range(i,0,-1):
    if arr[j] < arr[j-1]:
      arr[j] , arr[j-1] = arr[j-1] , arr[j]
    else:
      break

print(arr)


```

## 카운팅 정렬 / 기수정렬
- 각 항목들의 발생 회수를 세고 정수 항목돌을 인덱스로 적용하는 정렬

### 안정성 확보법
- count 배열에 이전까지의 idx 값을 더하여 위치 값을 구한다.
- 기존 배열을 거꾸로 순환하며 count배열의 순서를 구해 새 배열에 넣는다. 

### 특징
- 시간복잡도 : O(n + k)
- 안정성 : O (누적합 계산시)
- 적응성 : X
- 제자리 정렬 : X
- N이 크고 K 가 작을때 효과적


### 코드 
```python
arr = [4,6,3,7,8,8,8,5,3]
counts = [0] * max(arr) + 1
temp = [0]* len(arr)

for num in arr:
  counts[num] += 1

for i in range(1, len(counts)):
  counts[i] += counts[i-1]

for i in range(len(arr)-1,-1,-1):
  val = arr[i]
  temp[counts[val]-1] = val
  counts[val] -= 1

print(temp)

```

## 퀵 정렬
## 병합 정렬
