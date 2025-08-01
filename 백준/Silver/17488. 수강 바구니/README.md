# [Silver IV] 수강 바구니 - 17488 

[문제 링크](https://www.acmicpc.net/problem/17488) 

### 성능 요약

메모리: 43952 KB, 시간: 764 ms

### 분류

구현, 정렬

### 제출 일자

2025년 7월 27일 02:12:03

### 문제 설명

<p>건국대학교 학생들은 수강신청 전에 수강바구니를 통해 미리 수강신청을 할 수 있다. 수강바구니는 수강신청과 마찬가지로 각 과목마다 수강제한인원이 정해져 있다.</p>

<p>수강바구니는 1차와 2차로 나누어 진행한다. 수강바구니 기간동안 학생들은 원하는 과목들을 자신의 수강바구니에 담을 수 있다.</p>

<p>1차 수강바구니 기간이 종료되면, 과목별로 수강제한인원을 초과하지 않는 한 수강등록이 완료된다. 2차 수강바구니의 수강제한인원은 1차 수강바구니의 수강등록이 완료된 후 남는 자리가 된다. 수강바구니가 종료된 시점에서 각 학생들의 수강바구니는 초기화되지 않는다.</p>

<p>학생 <em>N</em>명이 <em>M</em>개 과목의 수강바구니에 참여하고 1차, 2차 수강바구니에 담은 과목들이 각각 주어질 때, 학생별로 수강바구니를 통해 수강신청에 성공한 과목을 출력하자.</p>

### 입력 

 <p>첫 줄에 두 자연수<em> N</em>, <em>M</em>이 공백으로 구분돼 주어진다. 각각 학생과 과목의 수를 의미한다.</p>

<p>둘째 줄에 각 과목별의 수강제한인원 L<sub>1</sub>, L<sub>2</sub>, ..., L<sub>M</sub>이 공백으로 구분돼 주어진다.</p>

<p><em>2×N</em>개의 줄에 걸쳐 수강바구니의 신청 쿼리가 주어진다. 앞선<em> N</em>개의 줄에는 1번 학생, 2번 학생, …, <em>N</em>번 학생이 1차 수강바구니에 넣은 과목들이, 이어지는 <em>N</em>개에 줄에는 2차 수강바구니에 넣은 과목들이 주어진다.</p>

<p>신청 쿼리의 끝에는 -1이 입력되며, 한 학생이 같은 과목을 중복하여 담는 경우는 없다.</p>

### 출력 

 <p>첫째 줄부터<em> N</em>개의 줄에 걸쳐 1번 학생이 수강등록에 성공한 과목, 2번 학생이 수강등록에 성공한 과목, …,<em> N</em>번 학생이 수강등록에 성공한 과목을 공백으로 구분해 오름차순으로 출력한다. 수강등록에 성공한 과목이 없는 경우 “망했어요” (따옴표 제외)를 대신 출력한다.</p>

