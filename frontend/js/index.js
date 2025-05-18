async function fetchElectricCarbonFactor() {
    let apiUrl = $('#api-endpoint').val();
    apiUrl = '/api/v1/electric_carbon_factor';
    await $.ajax({
        url: apiUrl,
        method: 'GET',
        headers: {'Accept': 'application/json'},
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

async function calculateElectricCarbonFactor() {

}
