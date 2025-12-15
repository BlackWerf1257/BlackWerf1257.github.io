---
layout: post
title: React - Web Storage API
tags: [React]
---

## Web Storage API



### 정의

- 웹의 데이터를 클라이언트에 저장할 수 있는 자료 구조
- SessionStorage와 LocalStorage 2가지가 존재함
- **키/값** 쌍으로 데이터를 저장하고, 키를 기반으로 데이터를 조회하는 자료 구조

<br>

### 종류

#### SessionStorage

- 브라우저가 유지되어 있는 동안 데이터를 유지하는 자료 구조
  - 브라우저를 새로 열 경우, 데이터가 삭제됨

#### LocalStorage 

- sessionStorage와 동일하지만, 브라우저를 다시 열어도 데이터가 유지되는 자료 구조
- 유효기간의 제한없이 저장이 가능하며, 캐시나 로컬 저장 데이터를 지워야 삭제됨

<br>

### 사용 방법

~~~react
//데이터의 저장
sessionStorage.setItem("키의 이름", 데이터);
localStorage .setItem("키의 이름", 데이터);

//예시
sessionStorage.setItem("SboolLogged", isLogged);
localStorage.setItem("SboolLogged", isLogged);


//데이터의 조회
sessionStorage.getItem("키의 이름");
localStorage.getItem("키의 이름");

//예시
sessionStorage.getItem("SboolLogged");
localStorage.getItem("SboolLogged");


//데이터의 삭제
sessionStorage.removeItem('키의 이름');
localStorage.removeItem('키의 이름');

//예시
sessionStorage.removeItem('키의 이름');
localStorage.removeItem('키의 이름');

~~~

<br><br><br><br><br><br><br><br><br><br><br>

---

**참고한 자료**

[[React] LocalStorage 데이터 저장하기](https://velog.io/@jay_be/React-LocalStorage-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0) 
