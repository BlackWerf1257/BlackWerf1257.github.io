+++
title = "React - Communicating with the Server"
weight = 7
sort_by = "weight"
[extra]
+++
## Communicating with the Server

※This post implements the solution using only Fetch and FormData, without Axios.

### REST API

#### Definition

- The communication method (interface) used by two computers to exchange information over the Internet

What is REST?

- Representational State Transfer, an acronym for a software architecture that defines the transmission and processing of data over a network. - Using this approach enables the implementation and modification of stable communication even in large-scale systems and multi-platform environments.

#### Benefits

Scalability

- REST handles interactions between clients and servers, providing benefits in performance improvement and scalability.

##### Flexibility

- RESTful services support complete client-server separation, providing flexibility where platform or technology changes on the server do not affect the client. - Complete separation between server and client enables changes to the database layer or other components without requiring application modifications.

##### Independence

- REST APIs operate independently of the underlying technology, enabling application implementation in various programming languages and allowing technology changes without affecting communication.

#### Composition

##### Unique Resource Identifier

- URLs are used to uniquely identify each resource - **Example)** http://testsite.com/posts/post1

##### Method

###### Types

- **GET** - Used to retrieve data from the server - **Example)** Retrieving login and post information - **POST** - Used to add new data to the server - **Example)** Signing up and creating a new post
- **PUT** - Used to modify existing data - **Example)** Updating user data, editing posts - **DELETE** - Used to remove data from the server - **Example)** Account deletion, removing posts/comments

##### HTTP Headers

- Data required for HTTP methods to function - Contains information such as the request method, authentication credentials, and content type.

Parameters

- Path parameters (**URL**) - Query parameters requesting additional information about a resource - Cookie parameters for fast client authentication

#### Structure of the Response

##### Status Bar

Two hundred

- Indicates **Response Success**

###### 201

- Indicates a successful response to a POST method

###### 4XX

- **An invalid request that the server cannot process**

###### 404

- **Resource Not Accessible**

##### Message Body

- Refers to a message containing a resource representation, typically returned in XML or JSON format. 

  The following is an example of JSON-formatted data for the above.

json { "id":"testId1", "pwd":"testPwd1", "userName":"testUserName1" }

##### Header

- This includes headers/metadata for the response, containing information such as encoding, date, and content type.

### Required Elements

#### Fetch

##### Definition

- An internal library in JavaScript that handles asynchronous communication with the server.[^1]

#### FormData

##### Definition

- An object for handling key/value data in the same manner as form fields - Data transmission is possible using the **XMLHttpRequest.send()** method - For GET requests, it can be used by passing it directly to the URLSearchParams constructor

##### Method

- **FormData.append()**: Adds a new value to an existing key, or adds a new key and value if the key does not exist. - **FormData.delete()**: Deletes a key/value pair from the FormData object. - **FormData.entries()**: Returns an iterator that can retrieve all key/value pairs.
- **FormData.get()**: Returns the first value that satisfies the key condition. - **FormData.getAll()**: Returns all values that satisfy the key condition as an array. - **FormData.has()**: Returns a boolean indicating whether a specific key exists.
- **FormData.keys()**: Returns an iterator over all keys - **FormData.set()**: Sets a new value for an existing key or adds a new key/value pair - **FormData.values()**: Returns an iterator over all values

##### How to Use

react const formData = new FormData(); // Create a new FormData object formData.append('id', 'tId1'); formData.append('id', 'tId2'); // Store values in the format id=tId1, id=tId2

formData.get("id"); // Returns only the first value, tId1


//Example code for sending data fetch('/url', { method: "POST", body: formData });

1. Create a new FormData object using new FormData(). 2. Use the append()/get() methods to create, retrieve, or modify values. 3. As shown in the example code above, you can transmit the FormData object using methods like fetch or response.

For more details, please refer to this [link](https://ko.javascript.info/formdata).

Courses

#### Definition

- Cross-Origin Resource Sharing (CORS), an abbreviation for Cross-Origin Resource Sharing, refers to the mechanism that enables web pages to access resources from other sites.

- JavaScript restricts requests to other domains for security reasons (same-origin policy). To resolve this, you need to set up CORS.

  - If CORS does not exist, security issues such as sending fake client requests from other applications may arise.

- CORS operates as follows.

  1. The browser adds an Origin header to the request containing the protocol, host, and port information of the current path. 2. The server checks the Origin header and responds with the requested data and an Access-Control-Allow-Origin header.
  3. The browser checks the Access-Control-Request header and shares the returned data with the client application. 4. If the server does not allow cross-origin access, it returns an error message.

  ##### Same-Origin Policy

  - Browsers only allow clients to request resources from the same origin. - Requests are only permitted when the client's URL matches the server's protocol, port, and host exactly. - Example: Client URL: http://127.0.0.1:3000

  | URL | Success Status | Type | Failure Reason | | -------------------------------- | :-------: | :---------: | :---------: | | http://127.0.0.1:3000/login.html | O | Same origin | |
  | http://127.0.0.1:4000/main.html | X | Different origin | Different port | | http://126.0.0.1:3000/main.html | X | Different origin | Different host |

  - As shown in the example above, since the server requested by the client http://127.0.0.1:3000/login.html에서는 has the same host and port, the client's request is processed normally without error.
  - However, while the host is the same for http://127.0.0.1:4000/main.html은, the **port** is different, and the **host** is different from the client at http://126.0.0.1:3000/main.html는, so the client's request does not execute normally.

#### Method

##### Access-Control-Allow-Origin

- Setting specific origins to allow requests - **⁎**: Allow access from all origins 

###### How to Use

~~~react Access-Control-Allow-Origin: URL

//예시 header('Access-Control-Allow-Origin: http://127.0.0.1:3000'); ~~~

##### Access-Control-Allow-Methods

- Setting the list of methods allowed on the server - GET, POST, PUT, DELETE, etc. are available[^2]

###### How to Use

~~~react Access-Control-Request-Method: method

//예시 header("Access-Control-Allow-Methods: POST"); ~~~

##### Access-Control-Allow-Headers

- Setting the list of allowed headers

###### How to Use

~~~react Access-Control-Request-Headers: HeaderType

//예시 header("Access-Control-Allow-Headers: Content-Type"); ~~~







#### CORS Preflight Request

- Due to the complexity of some HTTP requests in CORS interactions, method and header verification occurs before the actual request is sent. - While this typically happens automatically, preflight requests are omitted for simple requests. - Requests are sent in 2-3 configurations: Access-Control-Request-Method and Origin are mandatory, while Access-Control-Request-Headers are optional.

##### How It Works

- Example) When a DELETE request is made: 1. Before issuing the DELETE request, a preflight request is sent to verify whether the server permits DELETE. 2. If the server permits DELETE, it responds to the preflight request by including DELETE in the Access-Control-Allow-Methods header.



<br><br><br><br><br><br><br><br><br><br><br>

---

References

- [What is a RESTful API?](https://aws.amazon.com/ko/what-is/restful-api/)

- [FormData](https://developer.mozilla.org/ko/docs/Web/API/FormData)

- [The Infamous CORS Concept & Solutions - The Ultimate Guide](https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-CORS-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95-%F0%9F%91%8F)

- [Access-Control-Request-Method](https://developer.mozilla.org/ko/docs/Web/HTTP/Reference/Headers/Access-Control-Request-Method)

  <br><br><br><br><br><br><br><br><br><br><br>

[^1]: For more details on [fetch]({{ site.baseurl }}/posts/비동기와-동기화), please refer to the link.

[^2]: For more detailed information on HTTP request methods, please refer to [this link](https://developer.mozilla.org/ko/docs/Web/HTTP/Reference/Methods).

