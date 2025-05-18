async function fetchElectricCarbonFactor() {
    let apiUrl = $('#api-endpoint').val();
    apiUrl = '/api/v1/electric_carbon_factor';
    await $.ajax({
        url: apiUrl,
        method: 'GET',
        headers: {'Accept': 'application/json'},
    }).done((data) => {
        let electricCarbonFactor = data.data.data;
        let optionString = '';
        for (let index=0; index<electricCarbonFactor.length; index++) {
            optionString += `<option value="${electricCarbonFactor[index]['co2e']}">${electricCarbonFactor[index]['co2e']}(${electricCarbonFactor[index]['year']}年)</option>`;
        }
        $('#electric-carbon-factor').html(optionString);
    }).fail((jqXHR, textStatus, error) => {
        console.log(jqXHR);
        Swal.fire({
            'title': `錯誤，${textStatus}`,
            'text': error,
            'icon': 'error',
        });
    });
}

async function calculateElectricCarbonFactor() {
    let apiUrl = $('#api-endpoint').val();
    apiUrl = '/api/v1/calculate_electric';
    await $.ajax({
        url: apiUrl,
        method: 'POST',
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
        data: {
            'activity_data': Number($('#kwh-value').val()),
            'factor': Number($('#electric-carbon-factor').val()),
        },
    }).done((data) => {
        console.log(data);
    }).fail((jqXHR, textStatus, error) => {
        console.log(jqXHR);
        Swal.fire({
            'title': `錯誤，${textStatus}`,
            'text': error,
            'icon': 'error',
        });
    });
}
