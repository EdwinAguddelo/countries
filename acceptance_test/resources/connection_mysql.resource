*** Settings ***
Library     DatabaseLibrary
Library     OperatingSystem

*** Variables ***
${DBName}       %{db}
${DBHost}       %{host}
${DBPort}       %{port}
${DBUser}       %{user}
${DBPass}       %{password}
*** Keywords ***
Connect to database origen  
    ${output}   Connect To Database     pymysql     ${DBName}       ${DBUser}       ${DBPass}       ${DBHost}       ${DBPort}
    log to console  ${output}
    should be equal as strings   ${output}    None
    [Return]    ${output}