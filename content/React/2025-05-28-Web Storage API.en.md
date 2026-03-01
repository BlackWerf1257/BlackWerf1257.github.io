+++
title = "Web Storage API"
weight = 7
sort_by = "weight"
[extra]
+++
## Web Storage API



### Definition

- A data structure that can store web data on the client - Two types exist: SessionStorage and LocalStorage - A data structure that stores data as **key/value** pairs and retrieves data based on the key

<br>

### Types

#### SessionStorage

- A data structure that persists data while the browser remains open - When a new browser window is opened, the data is deleted

#### LocalStorage 

- A data structure identical to sessionStorage, but persists even after the browser is reopened - Can be stored without expiration restrictions and requires clearing the cache or local storage data to delete

<br>

### How to Use

react // Data storage sessionStorage.setItem("key name", data); localStorage.setItem("key name", data);

//예시 sessionStorage.setItem("SboolLogged", isLogged); localStorage.setItem("SboolLogged", isLogged);


// Retrieving data sessionStorage.getItem("key name"); localStorage.getItem("key name");

//예시 sessionStorage.getItem("SboolLogged"); localStorage.getItem("SboolLogged");


// Deleting data sessionStorage.removeItem('key name'); localStorage.removeItem('key name');

//Example sessionStorage.removeItem('key name'); localStorage.removeItem('key name');

~~~

<br><br><br><br><br><br><br><br><br><br><br>

---

**References**

[[React] Storing Data in LocalStorage](https://velog.io/@jay_be/React-LocalStorage-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0) 