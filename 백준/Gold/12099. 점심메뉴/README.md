# [Gold IV] 점심메뉴 - 12099 

[문제 링크](https://www.acmicpc.net/problem/12099) 

### 성능 요약

메모리: 122604 KB, 시간: 1060 ms

### 분류

정렬, 이분 탐색

### 제출 일자

2025년 7월 26일 12:20:38

### 문제 설명

<p>승관이와 영우는 앞으로 Q일 동안 점심을 같이 먹기로 했다. </p>

<p>승관이는 [u, v] 구간의 매운맛을 좋아하고 영우는 [x, y] 구간의 단맛을 좋아한다. (u, v, x, y는 매일 매일 기분 따라 바뀐다) </p>

<p>N가지 점심 메뉴의 매운맛 수치 a와, 단맛 수치 b가 주어지고, 앞으로 Q 일간의 u, v, x, y가 주어진다. </p>

<p>승관이와 영우의 점심 메뉴 선택을 돕기 위해, 날마다 승관이와 영우가 둘 다 좋아하는 메뉴의 수를 알려주는 프로그램을 만들어주자.</p>

### 입력 

 <p>입력의 첫 줄에 점심 메뉴의 수 N(1 ≤ N ≤ 10만)과, 점심을 같이 먹는 기간 Q(1 ≤ Q ≤ 5000)가 주어진다. </p>

<p>둘째 줄부터 N개의 줄에 각 메뉴의 매운맛, 단맛 수치인 a, b가 주어진다. (1≤ a, b ≤ 10억) </p>

<p>a, b값은 유니크하다. 즉 같은 a 값을 가지는 서로 다른 두 메뉴는 없고, 같은 b 값을 가지는 서로 다른 두 메뉴도 없다. </p>

<p>그 다음 줄부터 Q개의 줄에 각 날의 u, v, x, y가 주어진다. (1 ≤ u ≤ v ≤ 10억, v ≤ u + 10000, 1 ≤ x ≤ y ≤ 10억, y ≤ x + 10000) </p>

### 출력 

 <p>Q개의 줄에 줄마다 각 날의 영우와 승관이가 둘 다 좋아하는 메뉴의 수, 즉 u ≤ a ≤ v 이고, x ≤ b ≤ y 인 메뉴의 수를 출력한다 </p>

