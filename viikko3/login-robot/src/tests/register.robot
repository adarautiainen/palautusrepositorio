*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command  register kalle123
    Output Should Contain  User registered successfully


*** Keywords ***
Input New Command And Create User
    [Arguments]  ${username_password}
    ${username}  ${username} Split String  ${username_password}  ${SPACE}
    Input New Command  new ${username}  ${password}
    Run Keyword If  'User registered successfully'
