+++
title = "React - MUI"
weight = 7
sort_by = "weight"
[extra]
+++
More

What is MUI?

- An open-source React library that implements Google's Material Design.

### Features

#### Rapid Production

- Over 2,500 open-source contributors are participating in MUI.

#### Beauty

- Basic UI props provide beauty

#### Free Editing

- The library provides various customization features.

#### Team Collaboration

- Reducing barriers between backend developers and designers enables more effective collaboration

#### Used in various ways

- Launched in 2014, it boasts the largest community among React UI libraries.

### Types

#### Button

- A component that performs events through interactions with a single tab

- ##### Basic Structure

  react import Button from '@mui/material/Button'; //Required function buttonFunc() {   return(     <Button>Text</Button> //Basic structure     <Button varient="text">Text</Button> //Basic structure
      <Button variant="contained">Contained</Button> // Button with filled background design <Button variant="outlined">Outlined</Button> // Button with filled background design } export default buttonFunc;

  ##### Button Shape

  ###### Contained

  - Button with a filled background shape

  ###### Outlined

  - A button with only the outer border filled in

  ###### Text

  - Button that simply outputs text - Default

  ![Image Alt 텍스트](assets/img/React/MUI/default_button_design.png)

  ##### Color

  - Can be specified using the **color** attribute, and multiple default colors can be set.

    - ###### primary

      - Default theme color

    - ###### secondary

      - Secondary Theme Color

    - ###### error

      - Red-based colors

    - ###### warning

      - Orange-based colors

    - ###### info

      - Blue-toned colors

    - ###### success

      - Green-toned colors

  - **However**, to use custom colors, you must specify the style within the sx attribute, like **sx={{color: red}}**.

  - ###### Example

  ~~~react <Button color="error" variant="outlined">오류</Button> //프리셋 컬러 <Button variant="outlined" sx={{color:"red"}}>빨간 버튼</Button> ~~~

  ![Image Alt 텍스트](assets/img/React/MUI/button_color.png)

  - For more details, please refer to [here](https://mui.com/material-ui/customization/palette/#custom-colors).

  ##### Size

  - Can be specified using the **size** property

  - ###### Types

    - small - medium - large

    ~~~ <Button variant="outlined" size='small'>버튼</Button> <Button variant="outlined" size='medium'>버튼</Button> <Button variant="outlined" size='large'>버튼</Button> ~~~

    ![Image Alt 텍스트](assets/img/React/MUI/button_size.png)

    <br><br>

  - For additional details, please refer to [here](https://mui.com/material-ui/customization/palette/#custom-colors).

#### Text Field

- UI types that accept user input

- Supports input of various data types, including text and file attachments

- ###### Basic Structure

  ~~~react <TextField varient="outlined"></TextField> ~~~

variant

  - outlined - default when variant is omitted - Input field with underlined design - filled - Input field with a rectangular shape and light gray background color - standard - Input field with a rectangular shape

- ###### Form Props

  - A prop that provides information about data to be entered, such as ID/password - Includes properties like required, disabled, read only - **required**: Mandatory input - **disabled**: Input field is inactive - **read only**: Data within the input field cannot be modified

- ##### validation

  - As a prop for the error state, it enables providing feedback to the user, such as data type mismatches.

- ##### Multiline (multiple line input)

  - Changing the MUI Base TextArea to AutoSize - If **rows** is not used, the height automatically adjusts to fit the entered data - minRows and maxRows can be used to set the minimum/maximum number of rows

#### Progress

- A prop used to indicate that a task is in progress, utilizing a spinner.

  - **However**, customization is also possible in forms such as bars.

- **※Caution** - Due to high CPU usage and re-rendering every 200ms, it is advisable to avoid excessive use.

- ##### color

  - secondary, success, inherit, etc. exist

- ##### to you

  - Unlike buttons, sizes can be specified using px, rem, etc. - **Example**

  ~~~react <CircularProgress size="20px"/> ~~~

- ##### value

  - Used to adjust the fill level of the progress bar

  - To fill the progress bar in a fixed state, you must set the variant to **determinate**.

  - You can specify values using **value={value}**.

  - When progress is specified for a value, the value changes in accordance with the completion percentage of the task.

    - Example

      ~~~react <CircularProgress variant='determinate' value={25} /> ~~~

##### LinearProgress

- Straight-line progress bar - Can be used with **LinearProgress**

#### Box

- A container-type component that wraps other components

- Primarily used to wrap specific components and apply styles

- A component that combines additional functionality with a **div**. 

- ##### Basic Structure

~~~ {% raw %} <Box sx= {{ width: 100, height: 100, borderRadius: 1 m: 2 }} /> {% endraw %} ~~~



- **width**: width

- **height**: Height

- **m**: Margin length on top, bottom, left, and right

  In addition to m, mt, mb, ml, and mr also exist.

- **borderRadius**: The radius of the component's rounded corners 

#### Grid

For more details, please refer to [here]({{ site.baseurl }}/posts/Grid).

---

References

[Material UI - Overview](https://mui.com/material-ui/getting-started/)

[Button](https://mui.com/material-ui/react-button/)

[Text Field](https://mui.com/material-ui/react-text-field/)

[Progress](https://mui.com/material-ui/react-progress/#circular-size)

[Box](https://mui.com/material-ui/react-box/) 