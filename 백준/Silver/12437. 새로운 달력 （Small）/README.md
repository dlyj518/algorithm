# [Silver IV] 새로운 달력 (Small) - 12437 

[문제 링크](https://www.acmicpc.net/problem/12437) 

### 성능 요약

메모리: 34536 KB, 시간: 32 ms

### 분류

구현, 수학, 정수론, 시뮬레이션

### 제출 일자

2025년 8월 2일 05:36:42

### 문제 설명

<p>태양계 밖에서 새로 발견된 행성 ELG8-G는 지구와는 다른 자전/공전주기를 가지고 있어서 지구의 달력을 그대로 가져다 쓸 수 없다. 이에 과학자들은 이 행성을 위해 새로운 달력 시스템을 만들기로 하였다. 그동안 지구에서 사용하던 그레고리력은 매달 날짜가 달라 다소 번거로운 점이 있어 이번 새로운 달력 시스템에서는 매달 같은 일수를 포함하도록 하였다. 이렇게 만들어 놓은 달력을 기반으로 매일 관찰한 내용을 기록하기 위해 커다란 달력을 만들기로 하였는데, 1년을 몇 달로 하는지, 1주를 며칠로 하는지에 따라서 달력이 크기가 달라진다는 사실을 알게 되었다. 이에 과학자들의 편의를 위해 기준이 되는 수들을 입력하면 필요로 하는 달력의 줄 수를 출력해 주는 프로그램을 작성하게 되었다.</p>

<p>달력은 다음과 같이 출력된다.</p>

<ul>
	<li>첫 달의 첫날은 첫 번째 열에 위치한다.</li>
	<li>첫 달을 제외한 각 달의 첫날은 이전달의 마지막 날 다음 열에 위치한다.</li>
	<li>서로 다른 달에 속한 날은 같은 줄에 위치하지 않는다.</li>
	<li>달력은 1년치만 출력된다.</li>
</ul>

<p>한 달에 11일이고, 1년에 3달이며, 한 주에 4일이면 다음과 같은 11줄짜리 달력이 만들어진다.  </p>

<table class="table table-bordered th-center td-center table-center-30">
	<tbody>
		<tr>
			<th>#0 </th>
			<th>#1 </th>
			<th>#2 </th>
			<th>#3</th>
		</tr>
		<tr>
			<td>1</td>
			<td>2</td>
			<td>3</td>
			<td>4</td>
		</tr>
		<tr>
			<td>5</td>
			<td>6</td>
			<td>7</td>
			<td>8</td>
		</tr>
		<tr>
			<td>9</td>
			<td>10</td>
			<td>11</td>
			<td> </td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>3</td>
			<td>4</td>
			<td>5</td>
		</tr>
		<tr>
			<td>6</td>
			<td>7</td>
			<td>8</td>
			<td>9</td>
		</tr>
		<tr>
			<td>10</td>
			<td>11</td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>3</td>
			<td>4</td>
			<td>5</td>
			<td>6</td>
		</tr>
		<tr>
			<td>7</td>
			<td>8</td>
			<td>9</td>
			<td>10</td>
		</tr>
		<tr>
			<td>11</td>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>입력의 첫 줄에는 테스트 케이스의 숫자 <strong>T</strong>가 주어진다. 아래로 T 줄의 입력이 주어지며 각 줄은 하나의 테스트 케이스에 대한 입력이다. 각 테스트 케이스는 아래와 같이 3개의 자연수로 주어진다.</p>

<pre>총월수 월당일수 주당일수
</pre>

### 출력 

 <p>각 테스트 케이스에 대한 출력은 "Case #x: y" 형태로 이루어져야 한다. x는 1부터 시작되는 케이스 번호이고, y는 달력을 만드는데 필요한 줄 수 이다.</p>

