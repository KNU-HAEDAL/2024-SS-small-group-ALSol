def solution(ary1, ary2) :   # 입력은 행렬곱을 위한 ary1, ary2
  # 행렬 초기화 : 행개수 = ary1의 행, 열개수 = ary2의 열
  res = [[0] * len(ary2[0]) for a in range(len(ary1))]

  # 행렬곱 ary1의 i행과 ary2의 j열을 곱하여 res의 i행j열에 저장
  for i in range (len(ary1)) :
      for j in range (len(ary2[0])) :
          for k in range (len(ary1[0])):
              res[i][j] += ary1[i][k] * ary2[k][j]
              
  # 결과 리스트 반환
  return res

# tester
print(solution([[1,4], [3,2], [4,1]], [[3,3], [3,3]]))