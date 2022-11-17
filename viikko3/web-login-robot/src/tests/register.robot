*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password_confirmation  pekka123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password_confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  matti
    Set Password  m
    Set Password_confirmation  m
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  matti
    Set Password  matti123
    Set Password_confirmation  matti456
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  matti
    Set Password  matti123
    Set Password_confirmation  matti123
    Submit Credentials
    Go To Login Page
    Set Login Username  matti
    Set Login Password  matti123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  jukka
    Set Password  fail
    Set Password_confirmation  fail
    Submit Credentials
    Go To Login Page
    Set Login Username  jukka
    Set Login Password  fail
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password_confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Set Login Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Login Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Login Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
