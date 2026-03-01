---
layout: post
title: React - MUI
tags: [React]

---

## MUI

### MUI란?

- 구글의 Material Design를 구현하는 오픈소스 리액트 라이브러리다

### 특징

#### 빠른 제작

- MUI에는 2500명 이상의 오픈소스 기여자가 참여중임

#### 아름다움

- 기본적인 UI 프롭이 아름다움을 제공함

#### 자유로운 수정

- 라이브러리에 다양한 커스터마이징 기능이 제공됨

#### 팀간 협업

- 백엔드 - 디자이너 간의 장벽을 줄여 더 효과적인 협업을 가능하게 함

#### 다양하게 사용됨

- 2014년에 시작되어, React UI 라이브러리 중 가장 큰 커뮤니티를 보유하고있음

### 종류

#### Button

- 단일 탭의 상호작용을 통하여 이벤트를 수행하는 컴포넌트

- ##### 기본 구조

  ~~~                                                                                                     react
  import Button from '@mui/material/Button';
  //필수
  
  function buttonFunc() {
      return(
  	<Button>Text</Button> //기본 구조
      <Button varient="text">Text</Button> //기본 구조
      <Button varient="contained">Contained</Button> //배경이 채워진 디자인의 버튼
      <Button varient="outlined">Outlined</Button> //배경이 채워진 디자인의 버튼    
      )
  }
  
  export default buttonFunc;
  ~~~

  ##### 버튼 모양

  ###### Contained

  - 배경이 채워진 모양의 버튼

  ###### Outlined

  - 바깥 테두리만 채워진 모양의 버튼

  ###### Text

  - 단순히 텍스트만 출력하는 버튼
  - 기본값임

  ![Image Alt 텍스트](assets/img/React/MUI/default_button_design.png)

  ##### 색상

  - **color** 속성을 이용하여 지정가능하며, 여러가지 디폴트 색 지정이 가능하다

    - ###### primary

      - 기본 테마 색상

    - ###### secondary

      - 보조 테마 색상

    - ###### error

      - 빨간 계열 색상

    - ###### warning

      - 주황 계열 색상

    - ###### info

      - 파랑 계열 색상

    - ###### success

      - 초록 계열 색상

  - **단**, 커스텀컬러를 사용하기 위해서는 **sx={{color: red}}**와 같이 sx 내부에 스타일을 지정해줘야한다

  - ###### 예시

  ~~~react
  <Button color="error" variant="outlined">오류</Button> //프리셋 컬러
  <Button  variant="outlined" sx={{color:"red"}}>빨간 버튼</Button>
  ~~~

  ![Image Alt 텍스트](assets/img/React/MUI/button_color.png)

  - 더 자세한 내용은 [여기](https://mui.com/material-ui/customization/palette/#custom-colors)를 참고바란다

  ##### 사이즈

  - **size** 프로퍼티를 이용하여 지정 가능하다

  - ###### 종류

    - small
    - medium
    - large

    ~~~
    <Button  variant="outlined" size='small'>버튼</Button>
            <Button  variant="outlined" size='medium'>버튼</Button>
            <Button  variant="outlined" size='large'>버튼</Button>
    ~~~

    ![Image Alt 텍스트](assets/img/React/MUI/button_size.png)

    <br><br>

  - 추가적인 내용은 [여기](https://mui.com/material-ui/customization/palette/#custom-colors)를 참고바란다

#### Text Field

- 사용자의 입력을 받는 유형의 UI

- 텍스트 / 파일 첨부 등 다양한 형태의 데이터 입력 받기가 가능하다

- ###### 기본 구조

  ~~~react
  <TextField varient="outlined"></TextField>
  ~~~

- ###### variant

  - outlined
    - vairant 생략시 기본값임
    - 밑줄 형태의 디자인의 입력창
  - filled
    - 사각형 도형에 옅은 회색 백그라운드 색의 입력창
  - standard
    - 사각형　도형의　입력창

- ###### Form Props

  - ID / 비밀번호등 입력할 데이터에 대한 정보를 제공하는 프롭
  - required, disabled, read only 등이 존재함
    - **required**: 필수 입력
    - **disabled**: 입력창 비활성화
    - **read only**: 입력창 내 데이터 수정 불가

- ##### validation

  - error state에 대한 프롭으로, 유저에게 데이터 유형 불일치와 같은 피드백 제공이 가능하다

- ##### Multiline(다중 줄 입력)

  - TextField를 MUI Base TextArea AutoSize 변경하는 것
  - **rows**를 사용하지 않을 경우, 높이가 입력한 데이터의 크기에 맞춰서 자동으로 맞춰진다
  - minRows, maxRows를 이용하여 최소/최대 줄의 설정이 가능하다

#### Progress

- 스피너를 이용하여, 작업의 처리 중을 알리는 목적으로 사용되는 프롭이다

  - **단**, 막대바 등의 형태로도 커스터마이징이 가능하다

- **※주의** - 높은 CPU 사용과 200ms마다 리렌더링되므로 남발하지 않는 것이 좋다

- ##### color

  - secondary, success, inherit 등이 존재한다

- ##### size

  - button과 다르게 px, rem등을 이용하여 사이즈 지정이 가능하다
  - **예시**

  ~~~react
  <CircularProgress size="20px"/>
  ~~~

- ##### value

  - 프로그레스바의 채우기 정도를 조절하는데 사용한다

  - 고정된 상태에서 프로그레스바를 채우기 위해서는 variant에 **determinate**를 지정해줘야한다

  - **value={값}**를 이용하여 값 지정이 가능하다

  - 값에 progress를 지정할경우 작업의 완료 비율에 대응하여 값이 변화한다

    - 예시

      ~~~react
      <CircularProgress variant='determinate' value={25} />
      ~~~

##### LinearProgress

- 직선 모양의 프로그레스바
- **LinearProgress**를 이용해 사용 가능함

#### Box

- 타 컴포넌트를 감싸는 컨테이너 형태의 컴포넌트

- 특정 컴포넌트를 감싸며 스타일을 적용하는데 주로 사용된다

- **div** 에 추가 기능을 합친 형태의 컴포넌트이다  

- ##### 기본 구조

~~~
{% raw %}
<Box
	sx= {{
	    width: 100,
	    height: 100,
	    borderRadius: 1
	    m: 2
	}}
/>
{% endraw %}
~~~



- **width**: 넓이

- **height**: 높이

- **m**: 상하좌우 여백 길이

  ​	m 이외에도 mt, mb, ml, mr이 존재함

- **borderRadius**: 컴포넌트의 둥근 길이 

#### Grid

자세한 내용은 [여기]({{ site.baseurl }}/posts/Grid)를 참고바란다

---

참고한 자료

[Material UI - Overview](https://mui.com/material-ui/getting-started/)

[Button](https://mui.com/material-ui/react-button/)

[Text Field](https://mui.com/material-ui/react-text-field/)

[Progress](https://mui.com/material-ui/react-progress/#circular-size)

[Box](https://mui.com/material-ui/react-box/)
