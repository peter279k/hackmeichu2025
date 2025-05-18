async function fetchElectricCarbonFactor() {
    let apiUrl = $('#api-endpoint').val();
    apiUrl += '/api/v1/electric_carbon_factor';
    await $.ajax({
        url: apiUrl,
        method: 'GET',
        headers: {'Accept': 'application/json'},
    }).done((data) => {
        let electricCarbonFactor = data.data.data.data;
        let optionString = '';
        for (let index=0; index<electricCarbonFactor.length; index++) {
            optionString += `<option value="${electricCarbonFactor[index]['co2e']}">${electricCarbonFactor[index]['co2e']} (${electricCarbonFactor[index]['year']}年)</option>`;
        }

        $('#calculate-carbon-value').attr('electric_carbon_factor', electricCarbonFactor[0]['co2e']);
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

async function calculateElectricCarbonFactor(electricCarbonFactor) {
    let apiUrl = $('#api-endpoint').val();
    apiUrl += '/api/v1/calculate_electric';
    await $.ajax({
        url: apiUrl,
        method: 'POST',
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
        data: JSON.stringify({
            'activity_data': Number($('#kwh-value').val()),
            'factor': Number(electricCarbonFactor),
        }),
    }).done((data) => {
        console.log(data.data);
        Swal.fire({
            'title': '計算結果',
            'text': data.data,
            'icon': 'success',
        });
    }).fail((jqXHR, textStatus, error) => {
        let errorMessage = error;
        if (jqXHR.responseJSON.detail) {
            errorMessage = jqXHR.responseJSON.detail[0].msg;
        }
        Swal.fire({
            'title': `錯誤，${textStatus}`,
            'text': errorMessage,
            'icon': 'error',
        });
    });
}
