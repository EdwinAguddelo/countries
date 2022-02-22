** Settings ***
Library     RequestsLibrary
Library     OperatingSystem
Library     DatabaseLibrary
Resource    ../resources/connection_mysql.resource

Suite Setup     Connect to database origen
Suite Teardown  Disconnect From Database

*** Variables ***
${url}      %{endpoint_population_density}   


*** Test Cases ***
Get_weatherInfo
    ${output}       query       select * from Log order by consultationDate desc
    log to console      ${output[0][0]}    
    ${response}     GET     ${url}      expected_status=200
    ${output2}       query      select * from Log order by consultationDate desc
    log to console      ${output2[0][0]}
    should be true      ${output2[0][0]} > ${output[0][0]}


    
